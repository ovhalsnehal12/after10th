import xml.etree.ElementTree as ET
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
    namespace = "http://www.sitemaps.org/schemas/sitemap/0.9"
    ET.register_namespace("", namespace)

    urlset = ET.Element(f"{{{namespace}}}urlset")

    pages = [
        "https://after10th.onrender.com/",
        "https://after10th.onrender.com/explore",
        "https://after10th.onrender.com/paths",
        "https://after10th.onrender.com/careers",
        "https://after10th.onrender.com/questions",
    ]

    for page in pages:
        url_element = ET.SubElement(
            urlset, f"{{{namespace}}}url"
        )
        loc = ET.SubElement(
            url_element, f"{{{namespace}}}loc"
        )
        loc.text = page

    xml_content = ET.tostring(
        urlset,
        encoding="utf-8",
        xml_declaration=True
    )

    return Response(
        xml_content,
        status=200,
        content_type="application/xml; charset=utf-8"
    )



if __name__ == "__main__":
    app.run(debug=True)
