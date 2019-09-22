from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, IntegerField, FieldList, BooleanField, FormField, DateField, TextAreaField, DecimalField, SelectField
from wtforms.validators import DataRequired, Email, NumberRange, ValidationError, Length, Optional
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
		purchaseitems = SelectField('How many purchases are you making?',
			validators=[DataRequired()],
			choices=[('0', 0), ('1', 1), ('2', 2), ('3', 3), ('4', 4), ('5', 5)])
		funditems = SelectField('How many fundraisers are you planning?',
			validators=[DataRequired()], 
			choices=[('0', 0), ('1', 1), ('2', 2), ('3', 3), ('4', 4), ('5', 5)])
		submit = SubmitField('Submit')
		
	return ClubNameMinutesForm()

class PurchaseOrderForms(FlaskForm):
	payable_to = StringField('Payable To')
	amount = DecimalField('Amount', places=2,
		render_kw={"placeholder":"00.00"})
	expenditure = StringField('Purpose of Expenditure', 
		render_kw={"placeholder":"Expenditure"})

class FundraiserForms(FlaskForm):
	descript = StringField('Fundraiser Description',
		validators=[Optional()])
	proposeddate = DateField('Proposed Date (dd/mm/year)',
			validators=[Optional()],
			format = '%d/%m/%Y')
	expenditure = StringField('Purpose of Expenditure',
		validators=[Optional()],
		render_kw={"placeholder":"Expenditure"})

class MotionForms(FlaskForm):
	motionedby = StringField('Motioned By',
	    validators=[Optional()],
        render_kw={"placeholder":"Name"})
	secondby = StringField('Seconded By',
		validators=[Optional()],
		render_kw={"placeholder":"Name"})
	numfor = IntegerField('Number For',
		validators=[Optional()],
		render_kw={"placeholder":"#"})
	numagainst = IntegerField('Number Against',
		validators=[Optional()],
		render_kw={"placeholder":"#"})

def create_club_minutes_form(club, purchase, fund):
	num_members = len(club.members)
	class ClubMinutesForm(FlaskForm):
		date = DateField('Meeting Date (mm/dd/year)',
			validators=[DataRequired(), DateRange(max = date.today())],
			format = '%m/%d/%Y')
		time = TimeField('Meeting Called to Order at')
		location = StringField('Meeting Place',
			validators=[DataRequired()],
			render_kw={"placeholder":"Room # or Area"})
		attendance = FieldList(BooleanField('Here'),
			min_entries=num_members,
			max_entries=num_members)
		purchaseform = FieldList(FormField(PurchaseOrderForms), 
			min_entries=purchase, 
			max_entries=purchase)
		purchasevote = FormField(MotionForms)
		fundform = FieldList(FormField(FundraiserForms), 
			min_entries=fund, 
			max_entries=fund)
		fundvote = FormField(MotionForms)
		notes = TextAreaField('Overview of Meeting', 
			validators=[DataRequired(), Length(min=10, max=500)])
		submit = SubmitField('Submit')
		
	return ClubMinutesForm()

def view_club_name_form(user):
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
