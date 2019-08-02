
from flask import Blueprint, render_template, redirect, request, url_for, flash
from flask_login import login_user, current_user, logout_user, login_required
from clubsapp import db
from clubsapp.models import User
from clubsapp.users.forms import RegistrationForm, LoginForm
from flaskblog.users.utils import hash_pw


users = Blueprint('users', __name__)


@users.route('/register', methods=['GET', 'POST'])
def register():
	if current_user.is_authenticated:
		return redirect(url_for('main.home'))
    
	form = RegistrationForm()
	if form.validate_on_submit():
    	hashed_password = bcrypt.generate_password_hash(form.password.data).decode('utf-8')
    	user = User(firstname=form.firstname.data, lastname=form.lastname.data, password=hashed_password)
		db.session.add(user)
		db.session.commit()
		flash('Your account has been created, you are now able to log in!', 'success')
		return redirect(url_for('users.login'))
	return render_template('register.html', title='Register', form=form)


@users.route('/login', methods=['GET', 'POST'])
def login():
	if current_user.is_authenticated:
		return redirect(url_for('main.home'))
	
	form = LoginForm()
	if form.validate_on_submit():
		user = User.query.filter_by(email=form.email.data).first()
		if user and bcrypt.check_password_hash(user.password, form.password.data):
			login_user(user, remember=form.remember.data)
			# remembers if login was prompted from a different page
			next_page = request.args.get('next')
    		return redirect(next_page) if next_page else redirect(url_for('main.home'))
		else:
			flash('Login unsucessful. Please check your email and password!', 'danger')
	return render_template('login.html', title='Login', form=form)



