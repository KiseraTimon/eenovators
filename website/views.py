from flask import Blueprint, render_template, url_for, session, redirect

views = Blueprint('views', __name__)

@views.route('/')
def homepage():
    return render_template("home/index.html")

# Under construction pages
@views.route('/404')
def comingsoon():
    return render_template('other/comingsoon.html')

@views.route('/about')
def about():
    return render_template('other/comingsoon.html')

@views.route('/services')
def services():
    return render_template('other/comingsoon.html')

@views.route('/contact')
def contact():
    return render_template('other/comingsoon.html')

@views.route('/blog')
def blog():
    return render_template('other/comingsoon.html')

@views.route('/studies')
def studies():
    return render_template('other/comingsoon.html')

@views.route('/whitepapers')
def whitepapers():
    return render_template('other/comingsoon.html')

@views.route('/FAQs')
def faqs():
    return render_template('other/comingsoon.html')