from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from flask_mail import Mail
from flask_assets import Environment, Bundle
from clubsapp.config import Config

db = SQLAlchemy()
login_manager = LoginManager()
login_manager.login_view = 'users.login'
login_manager.login_message_category = 'info'
mail = Mail()


# Make sure this is a good way to deal with this
js = Bundle('main.js', 'bootstrap.js',output='gen/all.js')

assets = Environment(app)
assets.register('all.js', js)


def create_app(config_class=Config):
  app = Flask(__name__)
  app.config.from_object(config_class)
  
  db.init_app(app)
  login_manager.init_app(app)
  
  # Import Blueprints
  
  
  return app
  