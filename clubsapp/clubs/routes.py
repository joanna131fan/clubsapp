from flask import Blueprint, render_template, url_for, redirect, request, flash
from flask_login import current_user, login_required
from clubsapp import db
from clubsapp.utils import ROLES
from clubsapp.models import Club, User, club_query
from clubsapp.clubs.forms import ClubRegistrationForm, ClubMinutes, AddMemberEntry


clubs = Blueprint('clubs', __name__)


@clubs.route('/user_clubs/<int:user_id>', methods=['GET', 'POST'])
@login_required
def user_clubs(user_id):
	user = User.query.get_or_404(user_id)
	clubs = user.clubs
	form = ClubRegistrationForm()
	if form.validate_on_submit():
		advisor = User.query.filter_by(email=form.email.data).first()
		# TODO: Change this back to `ROLES['teacher']`
		if not advisor or advisor.role != ROLES['student']: 
			flash('That email does not belong to an advisor, or does not exist at all!', 'danger')
      # what should this return?
			return render_template('user_clubs.html', clubs=clubs, user=user, form=form)
		club = Club(name=form.club_name.data)
		db.session.add(club)
		db.session.commit()
		club.members.append(advisor)
		flash('Your club has been created!', 'success')
		return render_template('user_clubs.html', clubs=clubs, user=user, form=form)
	return render_template('user_clubs.html', clubs=clubs, user=user, form=form)

# idk if this needs to know the user id?
@clubs.route('/club_members/<int:user_id>', methods=['GET', 'POST'])
@login_required
def club_members(user_id):
	user = User.query.get_or_404(user_id)
	clubs = user.clubs
	form = AddMemberEntry()
	if form.validate_on_submit():
		#TODO form validation and db stuffos
		pass
	return render_template('club_members.html', clubs=clubs, user=user, form=form)

@clubs.route("/record", methods=['GET', 'POST'])
@login_required
def record():
    form = ClubMinutes()
    return render_template('record.html', title='Record', form=form)

@clubs.route("/view")
@login_required
def view():
    return render_template('view.html', title='View')
