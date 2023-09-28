# flake8: noqa
import json
from flask import Flask, render_template
from flask_frozen import Freezer
from flask_flatpages import FlatPages

# Configurations
DEBUG = True
FLATPAGES_AUTO_RELOAD = DEBUG
FLATPAGES_EXTENSION = ".md"

app = Flask(__name__)
app.config.from_object(__name__)

# Flatpages extension
app.config["FLATPAGES_EXTENSION"] = ".md"
pages = FlatPages(app)

# Frozen-Flask freezer
freezer = Freezer(app)

# Load data from JSON file
with open("data/data.json", "r") as json_file:
    data = json.load(json_file)

socials = data.get("socials", [])
work_experience = data.get("work_experience", [])
education_data = data.get("education_data", [])
certification_data = data.get("certification_data", [])


# URL Routing for flat pages. Retrieves the page path from the URL and renders the page.
@app.route("/blog/<path:path>/")
def page(path):
    page = pages.get_or_404(path)
    return render_template("singlepost.html", page=page)


@app.route("/blog/")
def blog():
    return render_template("bloghome.html", pages=pages)


# All other routes.
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


@freezer.register_generator
def error_handlers():
    yield "/404/"


@app.errorhandler(404)
def page_not_found(e):
    return render_template("404.html"), 404


if __name__ == "__main__":
    app.run(debug=True)
