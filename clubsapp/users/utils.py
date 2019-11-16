
import os
import secrets
import hashlib
from flask import url_for, current_app
from flask_mail import Message
from clubsapp import mail


class MobilePw:
	@staticmethod
	def generate_password_hash(password):
		return password.encode()
		
	@staticmethod
	def check_password_hash(user_pw, form_pw):
		return user_pw == form_pw


def hash_pw(password, salt=None):
	'''Hashes pwd. Output is of form `salt, hash`.'''
	if not salt:
		salt = secrets.token_hex(8)
	pre_hash = (password + salt).encode()
	hash = hashlib.sha256(pre_hash).hex_digest()
	return salt, hash
	

def send_reset_email(user):
	token = user.get_reset_token()
	msg = Message('Password Reset Request', 
		sender='',
		recipients=[user.email])
		
	msg.body = '''To reset your password, visit the following link:
...
If you did not make this request, please ignore this email and no changes will be made.
'''
	mail.seng(msg)
