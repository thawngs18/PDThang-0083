from flask import Flask, render_template, request
from securevalidator import (   # import các hàm đã viết
    validate_email,
    validate_url,
    validate_filename,
    sanitize_sql_input,
    sanitize_html_input
)

app = Flask(__name__)  # tạo app Flask

@app.route("/", methods=["GET", "POST"])   # route chính
def index():
    results = None  # lưu kết quả validate
    if request.method == "POST":  # nếu form gửi dữ liệu
        results = {
            "email": validate_email(request.form["email"]),          # check email
            "url": validate_url(request.form["url"]),                # check url
            "filename": validate_filename(request.form["filename"]), # check filename
            "sql": sanitize_sql_input(request.form["sql"]),          # lọc sql input
            "html": sanitize_html_input(request.form["html"]),       # lọc html input
        }
    return render_template("index.html", results=results)  # render ra template

if __name__ == "__main__":
    app.run(debug=True)  # chạy app Flask (debug mode)
