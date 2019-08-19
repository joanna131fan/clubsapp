
from clubsapp.models import User
from clubsapp.utils import ROLES


def test_new_user():
	"""
	GIVEN a User model
	WHEN a new User is created
	THEN check the firstname, lastname, email, password, roles, and members
	"""
	user = User('Bob', 'White', 'BobWhite@gmail.com', 'password123!')
	assert user.firstname == 'Bob'
	assert user.lastname == 'White'
	assert user.email = 'BobWhite@gmail.com'
	assert user.password == 'password123!' # Check hashing later
	assert user.role == ROLES['STUDENT']
	assert user.members = []
