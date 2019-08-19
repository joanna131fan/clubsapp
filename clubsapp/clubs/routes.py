from flask import Blueprint, render_template, url_for, redirect, request, flash
from flask_login import current_user, login_required
from clubsapp import db
from clubsapp.utils import ROLES
from clubsapp.models import Club, User
from clubsapp.clubs.forms import ClubRegistrationForm, ClubMinutes, AddMemberEntry, create_member_entry_form


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
			# TODO: should this be a redirect?
			return render_template('user_clubs.html', clubs=clubs, user=user, form=form)
		club = Club(name=form.club_name.data)
		db.session.add(club)
		club.members.append(advisor)
		user.clubs.append(club)
		db.session.commit()
		flash('Your club has been created!', 'success')
		return render_template('user_clubs.html', clubs=clubs, user=user, form=form)
	return render_template('user_clubs.html', clubs=clubs, user=user, form=form)

# idk if this needs to know the user id?
@clubs.route('/club_members/<int:user_id>', methods=['GET', 'POST'])
@login_required
def club_members(user_id):
	user = User.query.get_or_404(user_id)
	form = create_member_entry_form(user)
	if form.validate_on_submit():
		club_to_join = form.club_name.data # Is actual Club instance
		for field in form.members:
			try:
				first, last = field.data.strip().split()
			except ValueError as e:
				continue # empty field
			member = User.query.filter_by(firstname=first, lastname=last).first()
			if member:
				member.clubs.append(club_to_join)
				db.session.commit()
			else:
				new_member = User(firstname=first, lastname=last, email=f'{first}.{last}fakemail', password='NO_ACCOUNT_USER')
				db.session.add(new_member)
				new_member.clubs.append(club_to_join)
				db.session.commit()
		return redirect(url_for('clubs.club_members', user_id=current_user.id))
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
