
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, IntegerField
from wtforms.validators import DataRequired, Email, ValidationError


class ClubRegistrationForm(FlaskForm):
    name = StringField('Club Name',
        validators=[DataRequired()],
        render_kw={"placeholder":"Enter Club Name"})
    advisor = StringField('Advisor',
        validators=[DataRequired()],
        render_kw={"placeholder":"Enter Advisor Name"})
    advisor_email = StringField('Advisor Email', 
        validators=[DataRequired(), Email()],
        render_kw={"placeholder":"Enter Advisor Email"})
    submit = SubmitField('Add Club')
    

