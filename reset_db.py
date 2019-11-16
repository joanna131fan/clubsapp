
from clubsapp import create_app, db


app = create_app()


if __name__ == '__main__':
	confirmation = '''Are you sure you want to restart the database?
WARNING: ALL DATA WILL BE LOST!
Type `RESTART` to restart.
Do anything else to cancel.
'''
	result = input(confirmation + '\n')
	if result == 'RESTART':
		print('RESTARTING...')
		with app.app_context():
			db.drop_all()
			db.create_all()
		print('DATABASE RESTARTED!')
	else:
		print('CANCELLED')
