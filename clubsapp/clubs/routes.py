
from flask import Blueprint, render_template, url_for, redirect, request, flash
from flask_login import current_user, login_required
from clubsapp import db
from clubsapp.models import Club, User
from clubsapp.clubs.forms import ClubRegistrationForm


clubs = Blueprint('clubs', __name__)


@clubs.route('/user_clubs/<int:user_id>', methods=['GET', 'POST'])
@login_required
def user_clubs(user_id):
	user = User.get_or_404(user_id)
	clubs = user.clubs
	form = RegisterClubForm()
	if form.validate_on_submit():
		advisor = User.query.filter_by(email=form.email.data)
		if not advisor:
			flash('That advisor email does not exist!', 'danger')
			return
		club = Club(name=form.name.data, bio='Default', advisor=advisor)
		db.session.add(club)
		db.session.commit()
		flash('Your club has been created!', 'success')
		return redirect('user_clubs.html', clubs=clubs, user=user, form=form)
	return render_template('user_clubs.html', clubs=clubs, user=user, form=form)


