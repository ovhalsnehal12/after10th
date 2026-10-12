
from flask import Flask, render_template, send_from_directory, Response
from datetime import date

app = Flask(__name__)


# Home Page
@app.route("/")
def home():
    return render_template("home.html")


# Explore Page
@app.route("/explore")
def explore():
    return render_template("explore.html")


# Education Paths Page
@app.route("/paths")
def paths():
    return render_template("paths.html")


# Careers Page
@app.route("/careers")
def careers():
    return render_template("careers.html")


# Questions Page
@app.route("/questions")
def questions():
    return render_template("questions.html")


# Google Search Console Verification
@app.route("/googledee485c4f05a4a5f.html")
def google_verification():
    return send_from_directory(
        app.root_path,
        "googledee485c4f05a4a5f.html"
    )


# XML Sitemap for Google
@app.route("/sitemap.xml")
def sitemap():
    pages = [
        "https://after10th.onrender.com/",
        "https://after10th.onrender.com/explore",
        "https://after10th.onrender.com/paths",
        "https://after10th.onrender.com/careers",
        "https://after10th.onrender.com/questions"
    ]

    xml = '<?xml version="1.0" encoding="UTF-8"?>\n'
    xml += '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n'

    for page in pages:
        xml += "  <url>\n"
        xml += f"    <loc>{page}</loc>\n"
        xml += f"    <lastmod>{date.today().isoformat()}</lastmod>\n"
        xml += "  </url>\n"

    xml += "</urlset>"

    return Response(xml, mimetype="application/xml")


if __name__ == "__main__":
    app.run(debug=True)
