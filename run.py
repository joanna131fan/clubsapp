from clubsapp import create_app
from clubsapp.config import Config, TestingConfig

if __name__ == '__main__':
	app = create_app(config_class=TestingConfig)	
	#TODO: check OS type and set debug to True
	debug = False if app.config['DEVICE_TYPE'] == 'iPad' else True
	app.run(debug=debug)
