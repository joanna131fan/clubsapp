
from flask import Blueprint, render_template, request
from flask_login import login_required


main = Blueprint('main', __name__)


@main.route("/")
@main.route("/home")
@login_required
def home():
	return render_template('home.html')


@main.route("/about")
@login_required
def about():
	return render_template('about.html', title='About')
