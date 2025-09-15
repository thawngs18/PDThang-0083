import unittest
from securevalidator import(
    validate_url,validate_email,validate_filename,
    sanitize_html_input,sanitize_sql_input
)

class TestValidators(unittest.TestCase):
    def setUp(self):
        print("\n Running: ",self._testMethodName)
    
    def test_validate_email_valid(self):
        self.assertTrue(validate_email("user@example.com"))
    
    def test_validate_email_valid(self):
        self.assertFalse(validate_email("user@@example.com"))

    def test_validate_url_valid(self):
        self.assertTrue(validate_url("https://example.com"))

    def test_validate_url_valid(self):
        self.assertFalse(validate_url("ftp://example.com"))

    def test_validate_filename_valid(self):
        self.assertTrue(validate_filename("report.pdf"))
    
    def test_validate_filename_valid(self):
        self.assertFalse(validate_filename("../../etc/passwd"))

    def test_sanitize_sql_input_injection(self):
        # input có SQL injection
        input_str = "' OR 1=1 --"
        sanitized = sanitize_sql_input(input_str)
        # kiểm tra không còn ký tự/từ khóa nguy hiểm
        self.assertNotIn("'", sanitized)      # không còn dấu nháy
        self.assertNotIn("--", sanitized)     # không còn comment
        self.assertNotIn("OR", sanitized.upper())  # không còn OR keyword

    def test_sanitize_sql_input_safe_text(self):
        # input text an toàn
        input_str = "hello world"
        sanitized = sanitize_sql_input(input_str)
        self.assertEqual(sanitized, "hello world")  # giữ nguyên

    def test_sanitize_html_input_script(self):
        # input chứa script XSS
        input_str = '<script>alert("XSS")</script>'
        sanitized = sanitize_html_input(input_str)
        # phải được escape an toàn
        self.assertEqual(
            sanitized,
            '&lt;script&gt;alert(&quot;XSS&quot;)&lt;/script&gt;'
        )

    def test_sanitize_html_input_safe_text(self):
        # input text an toàn
        input_str = "Hello World"
        sanitized = sanitize_html_input(input_str)
        

