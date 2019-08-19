from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, IntegerField, FieldList, BooleanField, FormField
from wtforms.validators import DataRequired, Email, ValidationError
from wtforms.widgets import Input
from clubsapp.models import Club, club_query
from wtforms_sqlalchemy.fields import QuerySelectField


def num_words(num):
	msg = f'Must be made up of exactly {num} words'

	def num_words_val(form, field):
		n = len(field.data.strip().split())
		if (n != num) and (n != 0):
			raise ValidationError(msg)

	return num_words_val


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


def create_member_entry_form(user):
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
			min_entries=5)
		submit = SubmitField('Add Members')
		
	return MemberEntryForm()


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


class ClubMinutes(FlaskForm):
	club_list = QuerySelectField(
		'Club Name', 
		validators=[DataRequired()],
		query_factory=club_query, 
		allow_blank=True, 
		get_label='name')

