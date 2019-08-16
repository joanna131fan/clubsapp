
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, IntegerField, FieldList, BooleanField, FormField
from wtforms.validators import DataRequired, Email, ValidationError
from wtforms.widgets import Input
from clubsapp.models import Club, club_query
from wtforms_sqlalchemy.fields import QuerySelectField


class ClubRegistrationForm(FlaskForm):
    club_name = StringField('Club Name',
        validators=[DataRequired()],
        render_kw={"placeholder":"Enter Club Name"})
    advisor = StringField('Advisor',
        validators=[DataRequired()],
        render_kw={"placeholder":"Enter Advisor Name"})
    email = StringField('Advisor Email', 
        validators=[DataRequired(), Email()],
        render_kw={"placeholder":"Enter Advisor Email"})
    submit = SubmitField('Add Club')
    
class AddMemberEntry(FlaskForm):
    club_name = QuerySelectField('Club Name', 
        validators= [DataRequired()],
        query_factory=club_query, 
        allow_blank=True, 
        get_label='name')
    member = FieldList(StringField('Member Name', 
        validators=[DataRequired()],
        render_kw={"placeholder": "Enter Full Name"}))
    submit = SubmitField('Add Members')

#class ClubMember(Field)

class ClubMinutes(FlaskForm):
    club_list = QuerySelectField('Club Name', 
        validators= [DataRequired()],
        query_factory=club_query, 
        allow_blank=True, 
        get_label='name')