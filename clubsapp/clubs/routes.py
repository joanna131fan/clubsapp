from flask import Blueprint, render_template, url_for, redirect, request, flash
from flask_login import current_user, login_required
from clubsapp import db
from clubsapp.utils import ROLES
from clubsapp.models import Club, User
from clubsapp.clubs.forms import ClubRegistrationForm, NumMembersToAddForm, create_member_entry_form, create_club_minutes_form, record_club_name_form


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
		# TODO: ADD CHECK UNIQUE CLUB
		db.session.add(club)
		club.members.append(advisor)
		user.clubs.append(club)
		db.session.commit()
		flash('Your club has been created!', 'success')
		return redirect(url_for('clubs.user_clubs', user_id=user_id))
	return render_template('user_clubs.html', clubs=clubs, user=user, form=form)


@clubs.route('/club_members/<int:user_id>', methods=['GET', 'POST'])
@login_required
def num_club_members(user_id):
	'''Allows users to select how many members they want to add.'''
	user = User.query.get_or_404(user_id)
	form = NumMembersToAddForm()
	if form.validate_on_submit():
		# send user to the add_club_members
		num_members = form.num_members.data
		return redirect(url_for('clubs.add_club_members', user_id=user_id, num_members=num_members))
	return render_template('num_club_members.html', user=user, form=form)

@clubs.route('/club_members/<int:user_id>/<int:num_members>', methods=['GET', 'POST'])
@login_required
def add_club_members(user_id, num_members):
	'''Allows user to add members to their club, based on output from previous form.'''
	user = User.query.get_or_404(user_id)
	form = create_member_entry_form(user=user, num_members=num_members)
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
		return redirect(url_for('main.home'))
	return render_template('add_club_members.html', clubs=clubs, user=user, form=form)

@clubs.route("/record_minutes/<int:user_id>", methods=['GET', 'POST'])
@login_required
def record_club_name(user_id):
	user = User.query.get_or_404(user_id)
	# TODO: use the same form
	form = record_club_name_form(user)
	if form.validate_on_submit():
		# send user to the record_club_minutes
        	club = form.club_list.data
        	return redirect(url_for('clubs.record_club_minutes', user_id=user_id, club_id=club.id))
	return render_template('record_club_name.html', title='Record', form=form, user=user)

@clubs.route("/record_minutes/<int:user_id>/<int:club_id>/record", methods=['GET', 'POST'])
@login_required
def record_club_minutes(user_id, club_id):
	user = User.query.get_or_404(user_id)
	club = Club.query.get_or_404(club_id)
	members = club.members
	form = create_club_minutes_form(club)
	if form.validate_on_submit():
		# actually update attendance here
		flash('Attendance updated successfully', 'success')
		return redirect(url_for('main.home'))
	
	return render_template('record_minutes.html', title='Record', form=form, user=user, members=members)

@clubs.route("/view")
@login_required
def view():
	return render_template('view.html', title='View')
