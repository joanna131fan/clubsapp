
from flask import Blueprint, render_template, redirect, request, url_for, flash
from flask_login import login_user, current_user, logout_user, login_required
from clubsapp import db
from clubsapp.models import User
from clubsapp.users.forms import RegistrationForm, LoginForm
from flaskblog.users.utils import hash_pw


users = Blueprint('users', __name__)


@app.route('/register', methods=['GET', 'POST'])
def register():
    if current_user.is_authenticated:
        return redirect(url_for('main.home'))
    
    form = RegistrationForm()
    if form.validate_on_submit():
        flash(f'Account created for {form.firstname.data}' {form.lastname.data}, 'success')
        return redirect(url_for('main.home'))
    return render_template('register.html', title='Register', form=form)


@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
      return redirect(url_for('main.home'))
    return render_template('login.html', title='Login', form=form)
