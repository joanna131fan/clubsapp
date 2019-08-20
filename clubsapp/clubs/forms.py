from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, IntegerField, FieldList, BooleanField, FormField
from wtforms.validators import DataRequired, Email, NumberRange, ValidationError
from wtforms.widgets import Input
from clubsapp.models import Club
from wtforms_sqlalchemy.fields import QuerySelectField

# --[ Validators
def num_words(num):
	msg = f'Must be made up of exactly {num} words'

	def num_words_val(form, field):
		n = len(field.data.strip().split())
		if (n != num) and (n != 0):
			raise ValidationError(msg)

	return num_words_val

# --[ Forms
class ClubRegistrationForm(FlaskForm):
	club_name = StringField(
		'Club Name',
		validators=[DataRequired()],
		render_kw={"placeholder": "Enter Club Name"})
	advisor = StringField(
		'Advisor',
		validators=[DataRequired()],
		render_kw={"placeholder": "Enter Advisor Name"})
	email = StringField(
		'Advisor Email',
		validators=[DataRequired(), Email()],
		render_kw={"placeholder": "Enter Advisor Email"})
	submit = SubmitField('Add Club')


class NumMembersToAddForm(FlaskForm):
	num_members = IntegerField(
		'Number of Members',
		validators=[DataRequired(), NumberRange(min=1, max=50)],
		render_kw={'placeholder': 'Enter # of Members'})
	submit = SubmitField('Submit')
	
	
def create_member_entry_form(user, num_members=5):
	def user_club_query():
		return user.clubs
	
	class MemberEntryForm(FlaskForm):
		club_name = QuerySelectField(
			'Club Name',
			validators=[DataRequired()],
			query_factory=user_club_query,
			allow_blank=True,
			get_label='name')
		members = FieldList(
			StringField('Member Name', 
			validators=[num_words(2)],
			render_kw={"placeholder": "Enter Full Name"}),
			min_entries=num_members,
			max_entries=num_members)
		submit = SubmitField('Add Members')
		
	return MemberEntryForm()

'''
class AddMemberEntry(FlaskForm):
	club_name = QuerySelectField(
		'Club Name', 
		validators=[DataRequired()],
		query_factory=club_query,
		allow_blank=True, 
		get_label='name')
	members = FieldList(
		StringField('Member Name', 
		validators=[num_words(2)], 
		render_kw={"placeholder": "Enter Full Name"}),
		min_entries=5)
	submit = SubmitField('Add Members')
'''

def create_club_minutes_form(user):
	def user_club_query():
		return user.clubs
	
	class ClubMinutesForm(FlaskForm):
		club_list = QuerySelectField(
			'Club Name',
			validators=[DataRequired()],
			query_factory=user_club_query,
			allow_blank=True,
			get_label='name')
		
	return ClubMinutesForm()
	
'''
class ClubMinutes(FlaskForm):
	club_list = QuerySelectField(
		'Club Name', 
		validators=[DataRequired()],
		query_factory=club_query, 
		allow_blank=True, 
		get_label='name')
'''
