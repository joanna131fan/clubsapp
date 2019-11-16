from flask import Flask
from flask_sqlalchemy import SQLAlchemy
no_bcrypt = False
try:
	from flask_bcrypt import Bcrypt
except ModuleNotFoundError as e:
	no_bcrypt = True
from flask_login import LoginManager
from flask_mail import Mail
if not no_bcrypt:
	from flask_assets import Environment, Bundle
from clubsapp.config import Config
import xlrd

db = SQLAlchemy()
if not no_bcrypt:
	bcrypt = Bcrypt()
login_manager = LoginManager()
login_manager.login_view = 'users.login'
login_manager.login_message_category = 'info'
mail = Mail()


# Make sure this is a good way to deal with this
if not no_bcrypt:
	js = Bundle('main.js', 'bootstrap.js',output='gen/all.js')


def create_app(config_class=Config):
	app = Flask(__name__)
	app.config.from_object(config_class)
	
	db.init_app(app)
	if app.testing:
		prepare_db(app)
	
	if not no_bcrypt:
		bcrypt.init_app(app)
	login_manager.init_app(app)
	mail.init_app(app)
	
	if not no_bcrypt:
		assets = Environment(app)
		assets.register('all.js', js)
	# Import Blueprints
	from clubsapp.main.routes import main
	from clubsapp.users.routes import users
	from clubsapp.clubs.routes import clubs
	app.register_blueprint(main)
	app.register_blueprint(users)
	app.register_blueprint(clubs)

	return app
	
	
	
def prepare_db(app):
	from clubsapp.models import User, Club
	
	with app.app_context():
		db.drop_all()
		db.create_all()
		
<<<<<<< HEAD
		test_student = User(firstname='Test', lastname='User', school='Portola High School', schoolid='21usertest', email='test@gmail.com', password='test')
		test_teacher = User(firstname='Test', lastname='Teacher', school='Portola High School', schoolid='teachertest', email='teacher@gmail.com', password='test')
=======
		test_student = User(firstname='Test', lastname='User', email='test@gmail.com', password='test')
		test_teacher = User(firstname='Test', lastname='Teacher', email='teacher@gmail.com', password='test')
>>>>>>> 571b656d3b3ad9b9da31363aeaae5115b7c7eb78
		test_club = Club(name='Test Club')
		db.session.add(test_student)
		db.session.add(test_teacher)
		db.session.add(test_club)
		test_club.members.extend([test_student, test_teacher])
		
		db.session.commit()
		db.session.close()
