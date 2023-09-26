# Generate deployment files for the website
from flask import Flask, render_template
from flask_frozen import Freezer
from views import views

# some configurations, ensure:
# 1. Pages are loaded on request
# 2. Page files are in markdown
DEBUG = True
FLATPAGES_AUTO_RELOAD = DEBUG
FLATPAGES_EXTENSION = ".md"

app = Flask(__name__)
app.register_blueprint(views, url_prefix="/")
app.config.from_object(__name__)
freezer = Freezer(app)


@app.errorhandler(404)
def page_not_found(e):
    return render_template("404.html"), 404


if __name__ == "__main__":
    app.run(debug=True, port=8000)
