# flake8: noqa
import json
from flask import Blueprint, render_template, redirect

views = Blueprint(__name__, "views")

# Load data from JSON file
with open("data/data.json", "r") as json_file:
    data = json.load(json_file)

socials = data.get("socials", [])
work_experience = data.get("work_experience", [])
education_data = data.get("education_data", [])
certification_data = data.get("certification_data", [])


@views.route("/")
def home():
    return render_template("index.html")


@views.route("/projects")
def projects():
    return (
        render_template("projects.html", socials=socials),
        200,
        {"content-type": "text/html; charset=utf-8"},
    )


@views.route("/cv")
def cv():
    return (
        render_template(
            "cv.html",
            experience=work_experience,
            education=education_data,
            certificates=certification_data,
        ),
        200,
        {"content-type": "text/html; charset=utf-8"},
    )


# @views.route("/blog")
# def blog():
#     return redirect("https://ismailkhan.hashnode.dev/")
