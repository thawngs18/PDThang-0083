import re            # regex
import html          # escape html
import urllib.parse  # parse url
import os            # basename, path utils

def validate_email(email: str) -> bool:
    """Kiểm tra format email (local@domain.tld)."""
    pattern = r'^[\w\.-]+@[\w\.-]+\.\w+$'        # local@domain.tld
    return re.fullmatch(pattern, email) is not None  # True nếu khớp

def validate_url(url: str) -> bool:
    """Chỉ chấp nhận http/https và phải có netloc (domain)."""
    try:
        parsed = urllib.parse.urlparse(url)     # tách scheme, netloc, path...
        return parsed.scheme in ('http', 'https') and bool(parsed.netloc)
    except Exception:
        return False                             # parse lỗi => ko hợp lệ

def validate_filename(filename: str) -> bool:
    """Ngăn path traversal: không cho '..' hoặc dấu / \\."""
    if '..' in filename or '/' in filename or '\\' in filename:
        return False                             # chứa ký tự nguy hiểm
    return os.path.basename(filename) == filename  # đảm bảo không có đường dẫn

def sanitize_sql_input(input_str: str) -> str:
    """Lọc ký tự/từ khóa SQL cơ bản (KHÔNG thay prepared statements)."""
    sanitized = re.sub(r"(--|;|:|['\"#])", "", input_str)  # bỏ ký tự nguy hiểm
    sanitized = re.sub(
        r"\b(OR|AND|SELECT|INSERT|DELETE|UPDATE|DROP|UNION|WHERE)\b",
        "",
        sanitized,
        flags=re.IGNORECASE
    )                                              # loại keyword
    return sanitized.strip()                       # trim

def sanitize_html_input(html_str: str) -> str:
    """Escape HTML để tránh XSS."""
    return html.escape(html_str)                   # & < > " -> entity tương ứng