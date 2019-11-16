from flask_wtf import FlaskForm
<<<<<<< HEAD
from wtforms import StringField, PasswordField, SubmitField, BooleanField, DateField, IntegerField, SelectField
=======
from wtforms import StringField, PasswordField, SubmitField, BooleanField, DateField, IntegerField
>>>>>>> 571b656d3b3ad9b9da31363aeaae5115b7c7eb78
from wtforms.validators import DataRequired, Length, Email, EqualTo, ValidationError
from wtforms.widgets import Input
from clubsapp.models import User


class RegistrationForm(FlaskForm):
    firstname = StringField('First Name', 
        validators=[DataRequired(), Length(min=2, max=10)],
        render_kw={"placeholder":"Enter First Name"})
    lastname = StringField('Last Name', 
        validators=[DataRequired(), Length(min=2, max=10)],
        render_kw={"placeholder":"Enter Last Name"})
<<<<<<< HEAD
    school = SelectField(u'High School',
        validators=[DataRequired()], choices=[('Portola High School', 'Portola High School'), ('Northwood High School', 'Northwood High School')])
    schoolid = StringField('School User Name', 
        validators=[DataRequired(), Length(min=2, max=60)],
        render_kw={"placeholder":"Enter User Name (example: 21nameuser)"})
=======
>>>>>>> 571b656d3b3ad9b9da31363aeaae5115b7c7eb78
    email = StringField('Email', 
        validators=[DataRequired(), Email()],
        render_kw={"placeholder":"Enter Email"})
    password = PasswordField('Password', 
        validators=[DataRequired(), EqualTo('confirm_password', message='Passwords Must Match')],
        render_kw={"placeholder":"Create Password"})
    confirm_password = PasswordField('Confirm Password', 
        validators=[DataRequired(), EqualTo('password', message='Passwords Must Match')],
        render_kw={"placeholder":"Confirm Password"})
    submit = SubmitField('Sign Up')
    
    def validate_email(self, email):
        user = User.query.filter_by(email=email.data).first()     
        if user:
            raise ValidationError('That email is taken, please choose another one')

    
class LoginForm(FlaskForm):
    email = StringField('Email', 
        validators=[DataRequired(), Email()],
        render_kw={"placeholder":"Enter Email"})
    password = PasswordField('Password', 
        validators=[DataRequired()],
        render_kw={"placeholder":"Enter Password"})
    remember = BooleanField('Remember Me')
    submit = SubmitField('Log In')
<<<<<<< HEAD

class RequestResetForm(FlaskForm):
    email = StringField('Email', 
        validators=[DataRequired(), Email()],
        render_kw={"placeholder":"Enter Email"})
    submit = SubmitField('Request Password Reset')

    def validate_email(self, email):
        user = User.query.filter_by(email=email.data).first()     
        if user is None:
            raise ValidationError('There is no account with that email. You must register first.')

class ResetPasswordForm(FlaskForm):
    password = PasswordField('Password', 
        validators=[DataRequired(), EqualTo('confirm_password', message='Passwords Must Match')],
        render_kw={"placeholder":"Create Password"})
    confirm_password = PasswordField('Confirm Password', 
        validators=[DataRequired(), EqualTo('password', message='Passwords Must Match')],
        render_kw={"placeholder":"Confirm Password"})
    submit = SubmitField('Reset Password')
=======
>>>>>>> 571b656d3b3ad9b9da31363aeaae5115b7c7eb78
