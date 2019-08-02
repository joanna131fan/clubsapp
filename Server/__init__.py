from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from flask_mail import Mail
from clubsapp.config import Config

db = SQLAlchemy()
login_manager = LoginManager()
login_manager.login_view = 'users.login'
login_manager.login_message_category = 'info'
mail = Mail()


def create_app(config_class=Config):
  app = Flask(__name__)
  app.config.from_object(config_class)
  
  db.init_app(app)
  login_manager.init_app(app)
  
  # Import Blueprints
  
  
  return app
  
