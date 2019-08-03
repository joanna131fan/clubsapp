
from flask import Blueprint, render_template, url_for, redirect, request, flash
from flask_login import current_user, login_required
from clubsapp import db
from clubsapp.models import Club, User
from clubsapp.clubs.forms import RegisterClubForm


clubs = Blueprint('clubs', __name__)


@clubs.route('/user_clubs/<int:user_id>', methods=['GET', 'POST'])
@login_required
def user_clubs(user_id):
	user = User.get_or_404(user_id)
	clubs = user.clubs
	form = RegisterClubForm()
	if form.validate_on_submit():
		club = Club(name=form.name.data, bio='Default')
		db.session.add(club)
		club.advisor = user
		db.session.commit()
		flash('Your club has been created!', 'success')
	return render_template('user_clubs.html', clubs=clubs, user=user, form=form)


