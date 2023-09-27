# Generate deployment files for the website
import json
from flask import Flask, render_template
from flask_frozen import Freezer

# some configurations, ensure:
# 1. Pages are loaded on request
# 2. Page files are in markdown
DEBUG = True
FLATPAGES_AUTO_RELOAD = DEBUG
FLATPAGES_EXTENSION = ".md"

app = Flask(__name__)
app.config.from_object(__name__)
app.testing = True
app.config["FREEZER_IGNORE_ENDPOINTS"] = ["/blog"]
# app.config["FREEZER_IGNORE_MIMETYPE_WARNINGS"] = True


freezer = Freezer(app)

# Load data from JSON file
with open("data/data.json", "r") as json_file:
    data = json.load(json_file)

socials = data.get("socials", [])
work_experience = data.get("work_experience", [])
education_data = data.get("education_data", [])
certification_data = data.get("certification_data", [])


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/projects/")
def projects():
    return (
        render_template("projects.html", socials=socials),
        200,
        {"Content-Type": "text/html; charset=utf-8"},
    )


@app.route("/cv/")
def cv():
    return (
        render_template(
            "cv.html",
            experience=work_experience,
            education=education_data,
            certificates=certification_data,
        ),
        200,
        {"Content-Type": "text/html; charset=utf-8"},
    )


# @app.route("/blog")
# def blog():
#     return redirect("https://ismailkhan.hashnode.dev/")


@app.errorhandler(404)
def page_not_found(e):
    return render_template("404.html"), 404


if __name__ == "__main__":
    app.run(debug=True)
