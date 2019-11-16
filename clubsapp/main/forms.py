from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, IntegerField, FieldList, BooleanField, FormField, DateField, TextAreaField, DecimalField, SelectField
from wtforms.validators import DataRequired, Email, NumberRange, ValidationError, Length, Optional
from wtforms_components import TimeField, DateRange
from wtforms.widgets import Input
from clubsapp.models import Club
from wtforms_sqlalchemy.fields import QuerySelectField
from datetime import datetime, date

# TODO: Fix select_school()
schools = [('Portola High School', '/Users/joannafan/Desktop/clubsproject/clubsapp/clubs/portolaclubs.xlsx'), 
('University High School', 'null'), ('Northwood High School', 'null'), 
('Irvine High School', 'null')
]
def select_school():
	def school_query():
		return schools

	class SchoolSelect(FlaskForm):
		school = QuerySelectField(
			'Club Name',
			validators=[DataRequired()],
			query_factory=school_query,
			allow_blank=True,
			get_label='name')
		submit = SubmitField('Select')
	return SchoolSelect()