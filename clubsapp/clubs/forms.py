
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, IntegerField
from wtforms.validators import DataRequired, Email, ValidationError
from wtforms.widgets import Input
from clubsapp.models import Club, club_query
from wtforms_sqlalchemy.fields import QuerySelectField


class ClubRegistrationForm(FlaskForm):
    name = StringField('Club Name',
        validators=[DataRequired()],
        render_kw={"placeholder":"Enter Club Name"})
    advisor = StringField('Advisor',
        validators=[DataRequired()],
        render_kw={"placeholder":"Enter Advisor Name"})
    email = StringField('Advisor Email', 
        validators=[DataRequired(), Email()],
        render_kw={"placeholder":"Enter Advisor Email"})
    submit = SubmitField('Add Club')
    
class ClubMinutes(FlaskForm):
    club_list = QuerySelectField(query_factory=club_query, allow_blank=True, get_label='name') #Fix so submitted form cannot have blank club name
