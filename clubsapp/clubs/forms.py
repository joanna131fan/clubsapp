from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, IntegerField, FieldList, BooleanField, FormField, DateField, TextAreaField, DecimalField
from wtforms.validators import DataRequired, Email, NumberRange, ValidationError, Length
from wtforms_components import TimeField, DateRange
from wtforms.widgets import Input
from clubsapp.models import Club
from wtforms_sqlalchemy.fields import QuerySelectField
from datetime import datetime, date

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
		'Number of Members Being Added',
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


def record_club_name_form(user):
	def user_club_query():
		return user.clubs
	
	class ClubNameMinutesForm(FlaskForm):
		club_list = QuerySelectField(
			'Club Name',
			validators=[DataRequired()],
			query_factory=user_club_query,
			allow_blank=True,
			get_label='name')
		submit = SubmitField('Submit')
		
	return ClubNameMinutesForm()

class PurchaseOrderForms(FlaskForm):
	payable_to = StringField('Payable To')
	amount = DecimalField('Amount', places=2,
		render_kw={"placeholder":"00.00"})
	expenditure = StringField('Purchase of Expenditure', 
		render_kw={"placeholder":"Expenditure"})

class MotionForms(FlaskForm):
	motionedby = StringField('Motioned By',
		render_kw={"placeholder":"Name"})
	secondby = StringField('Seconded By',
		render_kw={"placeholder":"Name"})
	numfor = IntegerField('Number For')
	numagainst = IntegerField('Number Against')

def create_club_minutes_form(club):
	num_members = len(club.members)
	class ClubMinutesForm(FlaskForm):
		date = DateField('Meeting Date (dd/mm/year)',
			validators=[DataRequired(), DateRange(max = date.today())],
			format = '%d/%m/%Y')
		time = TimeField('Meeting Called to Order at')
		location = StringField('Meeting Place',
			validators=[DataRequired()],
			render_kw={"placeholder":"Room # or Area"})
		attendance = FieldList(BooleanField('Here'),
			min_entries=num_members,
			max_entries=num_members)
		purchaseform = FieldList(FormField(PurchaseOrderForms), 
			min_entries=5, 
			max_entries=5)
		purchasevote = FormField(MotionForms)
		notes = TextAreaField('Overview of Meeting', 
			validators=[DataRequired(), Length(min=10, max=400)])
		submit = SubmitField('Submit')
		
	return ClubMinutesForm()


