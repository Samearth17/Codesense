import flask
from flask import request, redirect, url_for, render_template
from functools import wraps

app = flask.Flask(__name__)
app.config["DEBUG"] = True

def login_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if "username" not in flask.session:
            return redirect(url_for("login", next=flask.request.url))
        return f(*args, **kwargs)
    return decorated_function

@app.route("/")
@login_required
def home():
    pages = [
        {"title": "Python", "slug": "python"},
        {"title": "JavaScript", "slug": "javascript"},
        {"title": "HTML/CSS", "slug": "html-css"}
    ]

    return render_template("cms.html", pages=pages)

@app.route("/login/", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        flask.session["username"] = request.form["username"]
        return redirect(url_for("home"))

    return render_template("login.html")

@app.route("/logout/")
def logout():
    flask.session.pop("username", None)
    return redirect(url_for("login"))

app.run()