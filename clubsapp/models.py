
from datetime import datetime
from itsdangerous import TimedJSONWebSignatureSerializer as Serializer
from flask import current_app
from flask_login import UserMixin
from clubsapp import db, login_manager


user_club_assoc_table = db.Table('user_club_assoc_table', 
  db.Column('user_id', db.Integer, db.ForeignKey('user.id')),
  db.Column('club_id', db.Integer, db.ForeignKey('club.id'))

)


class User(db.Model, UserMixin):
  id = db.Column(db.Integer, primary_key=True)
  firstname = db.Column(db.String(15), nullable=False)
  lastname = db.Column(db.String(15), nullable=False)
  email = db.Column(db.String(60), unique=True, nullable=False)
  password = db.Column(db.String(60), nullable=False)
  clubs = db.relationship('Club', secondary=user_club_assoc_table)

  
class Club(db.Model):
  id = db.Column(db.Integer, primary_key=True)
  name = db.Column(db.String(100), unique=True, nullable=False)
  members = db.relationship('User', secondary=user_club_assoc_table)
