
from flask import Flask, render_template, send_from_directory

app = Flask(__name__)


@app.route("/")
def home():
    return render_template("home.html")


@app.route("/explore")
def explore():
    return render_template("explore.html")


@app.route("/paths")
def paths():
    return render_template("paths.html")


@app.route("/careers")
def careers():
    return render_template("careers.html")


@app.route("/questions")
def questions():
    return render_template("questions.html")


# Google Search Console Verification Route
@app.route("/googledee485c4f05a4a5f.html")
def google_verification():
    return send_from_directory(
        app.root_path,
        "googledee485c4f05a4a5f.html"
    )


if __name__ == "__main__":
    app.run(debug=True)
