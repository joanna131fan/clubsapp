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
		return f'User(firstname={self.firstname!r}, lastname={self.lastname!r})'


class Club(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	name = db.Column(db.String(100), unique=True, nullable=False)
	members = db.relationship('User', secondary=user_club_assoc_table)

	def __repr__(self):
		return f'Club(name={self.name!r})'


def club_query():
	return Club.query

# class Minutes(db.Model): 
# 	id = db.Column(db.Integer, primary_key=True)
