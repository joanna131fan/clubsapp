from clubsapp import create_app


if __name__ == '__main__':
	app = create_app()	
	#TODO: check OS type and set debug to True
	debug = False
	if app.config['DEVICE_TYPE'] == 'MacBook':
		debug = True
	
	app.run(debug=debug)
