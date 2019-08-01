from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField, DateField, IntegerField
from wtforms.validators import DataRequired, Length, Email, EqualTo
from wtforms.widgets import Input

class RegistrationForm(FlaskForm):
    firstname = StringField('First Name', 
        validators=[DataRequired(), Length(min=2, max=10)],
        render_kw={"placeholder":"Enter First Name"})
    lastname = StringField('Last Name', 
        validators=[DataRequired(), Length(min=2, max=10)],
        render_kw={"placeholder":"Enter Last Name"})
    email = StringField('Email', 
        validators=[DataRequired(), Email()],
        render_kw={"placeholder":"Enter Email"})
    password = PasswordField('Password', 
        validators=[DataRequired()],
        render_kw={"placeholder":"Create Password"})
    confirm_password = PasswordField('Confirm Password', 
        validators=[DataRequired(), EqualTo('password')],
        render_kw={"placeholder":"Confirm Password"})
    submit = SubmitField('Sign Up')

class LoginForm(FlaskForm):
    email = StringField('Email', 
        validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    remember = BooleanField('Remember Me')
    submit = SubmitField('Log In')

class SubmitMinutes(FlaskForm):
    club = StringField('Club Name',
        validators=[DataRequired()],
        render_kw={"placeholder":"Enter Club Name"})
    advisor = StringField('Advisor',
        validators=[DataRequired()],
        render_kw={"placeholder":"Enter Advisor Name"})
    advisor_email = StringField('Advisor Email', 
        validators=[DataRequired(), Email()],
        render_kw={"placeholder":"Enter Advisor Email"})
    month = StringField('Month',
        validators=[DataRequired()],
        render_kw={"placeholder":"Month"})
    day = IntegerField('Day',
        validators=[DataRequired()],
        render_kw={"placeholder":"Day"})
    year = IntegerField('Year',
        validators=[DataRequired()],
        render_kw={"placeholder":"Year"})
    notes = StringField('Meeting Notes',
        validators=[DataRequired(), Length(min=0, max=300)],
        render_kw={"placeholder":"Max 300 Characters"})

