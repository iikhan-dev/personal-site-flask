# flake8: noqa
import json
from flask import Blueprint, render_template, redirect

views = Blueprint(__name__, "views")

# Load data from JSON file
with open("data/cv.json", "r") as json_file:
    data = json.load(json_file)

education_data = data.get("education_data", [])
certification_data = data.get("certification_data", [])
work_experience = data.get("work_experience", [])


@views.route("/")
def home():
    return render_template("index.html")


@views.route("/projects")
def projects():
    return render_template("projects.html")


@views.route("/cv")
def cv():
    return render_template(
        "cv.html",
        experience=work_experience,
        education=education_data,
        certificates=certification_data,
    )


@views.route("/blog")
def blog():
    return redirect("https://ismailkhan.hashnode.dev/")


@views.route("/resources")
def resources():
    return render_template("resources.html")
