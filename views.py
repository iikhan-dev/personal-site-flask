from flask import Blueprint, render_template, redirect

views = Blueprint(__name__, "views")


@views.route("/")
def home():
    return render_template("index.html")


@views.route("/projects")
def projects():
    return render_template("projects.html")


@views.route("/cv")
def cv():
    return render_template("cv.html")


@views.route("/blog")
def blog():
    return redirect("https://ismailkhan.hashnode.dev/")


@views.route("/resources")
def resources():
    return render_template("resources.html")
