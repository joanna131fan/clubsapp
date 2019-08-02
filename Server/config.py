
try:
  import environvars
  target = environvars.environ
 except ModuelNotFoundError as e:
  import os
  target = os.environ


class Config:
  SECRET_KEY = target['BLOG_SECRET_KEY'] or '97df9c8029f9e716e18088cb1db30e23'
  SQLALCHEMY_DATABASE_URI = target['BLOG_DB_URI']
  MAIL_SERVER = 'smtp.googlemail.com'
  MAIL_PORT = 587
  MAIL_USE_TLS = True
  MAIL_USERNAME = target['EMAIL_USER']
  MAIL_PASSWORD = target['EMAIL_APP_PASS']