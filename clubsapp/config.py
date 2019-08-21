
try:
	import environvars
	target = environvars.environ
except ModuleNotFoundError as e:
	import os
	target = os.environ


class Config:
	SECRET_KEY = target['CLUB_SECRET_KEY'] or '97df9c8029f9e716e18088cb1db30e23'
	SQLALCHEMY_DATABASE_URI = target['CLUB_DB_URI']
	MAIL_SERVER = 'smtp.googlemail.com'
	MAIL_PORT = 587
	MAIL_USE_TLS = True
	MAIL_USERNAME = target['EMAIL_USER']
	MAIL_PASSWORD = target['EMAIL_APP_PASS']
	DEVICE_TYPE = target['DEVICE_TYPE']
	WTF_CSRF_ENABLED = True

	
class TestingConfig(Config):
	SECRET_KEY = 'should_be_a_long_random_string'
	SQLALCHEMY_DATABASE_URI = 'sqlite:///testing.db'
	TESTING = True
	WTF_CSRF_ENABLED = False
