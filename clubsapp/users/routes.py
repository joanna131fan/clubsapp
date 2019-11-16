
from flask import Blueprint, render_template, redirect, request, url_for, flash
from flask_login import login_user, current_user, logout_user, login_required
<<<<<<< HEAD
from clubsapp import db, mail
=======
from clubsapp import db
>>>>>>> 571b656d3b3ad9b9da31363aeaae5115b7c7eb78
try:
	from clubsapp import bcrypt
except ImportError as e:
	# monkey-patch bcrypt lol
	from clubsapp.users.utils import MobilePw as bcrypt
from clubsapp.models import User
<<<<<<< HEAD
from clubsapp.users.forms import RegistrationForm, LoginForm, RequestResetForm, ResetPasswordForm
from clubsapp.users.utils import hash_pw
from flask_mail import Message
=======
from clubsapp.users.forms import RegistrationForm, LoginForm
from clubsapp.users.utils import hash_pw

>>>>>>> 571b656d3b3ad9b9da31363aeaae5115b7c7eb78

users = Blueprint('users', __name__)


@users.route('/register', methods=['GET', 'POST'])
def register():
	if current_user.is_authenticated:
		return redirect(url_for('main.home'))

	form = RegistrationForm()
	if form.validate_on_submit():
		hashed_password = bcrypt.generate_password_hash(form.password.data).decode('utf-8')
<<<<<<< HEAD
		user = User(firstname=form.firstname.data, lastname=form.lastname.data, school=form.school.data, schoolid=form.schoolid.data, email=form.email.data, password=hashed_password)
		db.session.add(user)
		db.session.commit()
		flash(f'Account has been created {form.firstname.data} {form.lastname.data} at {form.school.data}, you are now able to log in!', 'success')
=======
		user = User(firstname=form.firstname.data, lastname=form.lastname.data, email=form.email.data, password=hashed_password)
		db.session.add(user)
		db.session.commit()
		flash(f'Account has been created {form.firstname.data} {form.lastname.data}, you are now able to log in!', 'success')
>>>>>>> 571b656d3b3ad9b9da31363aeaae5115b7c7eb78
		return redirect(url_for('users.login'))
	return render_template('register.html', title='Register', form=form)

@users.route('/', methods=['GET', 'POST'])
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
			flash('Login unsuccessful. Please check your email and password!', 'danger')
	return render_template('login.html', title='Login', form=form)


@users.route('/logout')
def logout():
	logout_user()
	return redirect(url_for('users.login'))

<<<<<<< HEAD
def send_reset_email(user):
	token = user.get_reset_token()
	msg = Message('Password Reset Request', sender='noreply@clubsapp.com', recipients=[user.email]) #currently set to jaysee spam email
	msg.body = f'''To reset your password, visit the following link:
{url_for('users.reset_token', token=token, _external=True)}
	
If you did not make this request then simply ignore this email and no change will be made.
'''
	mail.send(msg)

@users.route('/reset_request', methods=['GET', 'POST'])
def reset_request():
	if current_user.is_authenticated:
		return redirect(url_for('main.home'))
	form = RequestResetForm()
	if form.validate_on_submit():
		user = User.query.filter_by(email=form.email.data).first()
		send_reset_email(user)
		flash('An email has been sent with instructions to reset your password.', 'info')
		return redirect(url_for('users.login'))
	return render_template('reset_request.html', title='Reset Password', form=form)

@users.route('/reset_password/<token>', methods=['GET', 'POST'])
def reset_token(token):
	if current_user.is_authenticated:
		return redirect(url_for('main.home'))
	user = User.verify_reset_token(token)
	if user is None:
		flash('That is an invalid or expired token', 'warning')
		return redirect(url_for('users.reset_request'))
	form = ResetPasswordForm()
	if form.validate_on_submit():
		hashed_password = bcrypt.generate_password_hash(form.password.data).decode('utf-8')
		user.password = hashed_password
		db.session.commit()
		flash(f'Your password has been updated, you are now able to log in!', 'success')
		return redirect(url_for('users.login'))
	return render_template('reset_token.html', title='Reset Password', form=form)
=======

>>>>>>> 571b656d3b3ad9b9da31363aeaae5115b7c7eb78
