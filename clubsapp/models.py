from datetime import datetime
from itsdangerous import TimedJSONWebSignatureSerializer as Serializer
from flask import current_app
from flask_login import UserMixin
from clubsapp import db, login_manager
from clubsapp.utils import ROLES
from flask_sqlalchemy import SQLAlchemy

user_club_assoc_table = db.Table('user_club_assoc_table',
	db.Column('user_id', db.Integer, db.ForeignKey('user.id')),
	db.Column('club_id', db.Integer, db.ForeignKey('club.id')))

roles = db.relationship('Role', secondary='user_roles',
                backref=db.backref('users', lazy='dynamic'))

@login_manager.user_loader
def load_user(user_id):
	return User.query.get(int(user_id))


class User(db.Model, UserMixin):
	id = db.Column(db.Integer, primary_key=True)
	firstname = db.Column(db.String(15), nullable=False)
	lastname = db.Column(db.String(15), nullable=False)
	email = db.Column(db.String(60), unique=True, nullable=False)
	password = db.Column(db.String(60), nullable=False)
	role = db.Column(db.Integer(), nullable=False, default=ROLES['student'])
	clubs = db.relationship('Club', secondary=user_club_assoc_table)
	
	def __repr__(self):
		return f'{self.firstname} {self.lastname}' #return f'User(firstname={self.firstname!r}, lastname={self.lastname!r})'


class Club(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	name = db.Column(db.String(100), unique=True, nullable=False)
	members = db.relationship('User', secondary=user_club_assoc_table)
	minutes = db.relationship('Minutes', backref='club')
	def __repr__(self):
		return f'Club(name={self.name!r})'

class Minutes(db.Model): 
	id = db.Column(db.Integer, primary_key=True)
	club_id = db.Column(db.Integer, db.ForeignKey('club.id'))
	date = db.Column(db.Date, nullable=False) #0000-00-00
	time = db.Column(db.Time) #00:00:00
	location = db.Column(db.String(100), nullable=False)
	attendance = db.relationship('Attendance', backref='minutes', lazy=True) #check code
	purchase =  db.Column(db.Text)
	purchasemotion = db.Column(db.Text)
	fundraiser = db.Column(db.Text)
	fundmotion = db.Column(db.Text)
	minute = db.Column(db.Text, nullable=False) #notes
	def __repr__(self):
		return f'{self.club_id} {self.date}'

class Attendance(db.Model):
	id = db.Column(db.Integer, primary_key=True, autoincrement=True)
	student_name = db.Column(db.String(35), nullable=False)
	minutes_id = db.Column(db.Integer, db.ForeignKey('minutes.id'))