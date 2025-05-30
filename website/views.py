from flask import Blueprint, render_template, url_for, session, redirect

views = Blueprint('views', __name__)

@views.route('/')
def homepage():
    return render_template("home/index.html")