from datetime import datetime
from itsdangerous import TimedJSONWebSignatureSerializer as Serializer
from flask import current_app
from flask_login import UserMixin
from clubsapp import db, login_manager


user_club_assoc_table = db.Table('user_club_assoc_table',
	db.Column('user_id', db.Integer, db.ForeignKey('user.id')),									db.Column('club_id', db.Integer, db.ForeignKey('club.id')))

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
	clubs = db.relationship('Club', secondary=user_club_assoc_table)
	roles = db.relationship('Role', secondary='user_roles', backref=db.backref('users', lazy='dynamic'))


class Role(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	name = db.Column(db.String(50), nullable=False, unique=True)
	
	
class UserRoles(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	user_id = db.Column(db.Integer, db.ForeignKey('user.id', ondelete='CASCADE'))
	role_id = db.Column(db.Integer, db.ForeignKey('role.id', ondelete='CASCADE'))


class Club(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	name = db.Column(db.String(100), unique=True, nullable=False)
	advisor_id = db.Column(db.Integer, db.ForeignKey('user.id'))
	advisor = db.relationship('User', back_populates='clubs')
	members = db.relationship('User', secondary=user_club_assoc_table)
	

