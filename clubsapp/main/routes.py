
from flask import Blueprint, render_template, request
from flask_login import login_required


main = Blueprint('main', __name__)


@main.route("/home")
@login_required
def home():
	news = ['Interclub Council Meeting 10/20', 
	'Homecoming 10/26', 
	'Clubapalooza 3/20'] #enter into excel
	return render_template('home.html', title='Home', news=news)


@main.route("/about")
@login_required
def about():
	return render_template('about.html', title='About')
