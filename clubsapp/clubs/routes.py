import pandas as pd
from flask import Blueprint, render_template, url_for, redirect, request, flash
from flask_login import current_user, login_required
from clubsapp import db
from clubsapp.utils import ROLES
from clubsapp.models import Club, User, Minutes, Attendance, Post
from clubsapp.clubs.forms import ClubRegistrationForm, NumMembersToAddForm, create_member_entry_form, create_club_minutes_form, record_club_name_form, view_club_name_form
import xlrd

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
	return render_template('user_clubs.html', clubs=clubs, user=user, form=form) #change to num_club_members


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
def generate_minutes(user_id):
	user = User.query.get_or_404(user_id)
	# TODO: use the same form
	form = record_club_name_form(user)
	if form.validate_on_submit():
		# send user to the record_club_minutes
            club = form.club_list.data
            purchitems = int(form.purchaseitems.data)
            funditems = int(form.funditems.data)
            return redirect(url_for('clubs.record_club_minutes', user_id=user_id, club_id=club.id, purchase=purchitems, fund=funditems))
	return render_template('record_club_name.html', title='Record', form=form, user=user)

#THERE MAY BE BUGS HERE 
@clubs.route("/record_minutes/<int:user_id>/<int:club_id>/<int:purchase>/<int:fund>/record", methods=['GET', 'POST'])
@login_required
def record_club_minutes(user_id, club_id, purchase, fund):
	user = User.query.get_or_404(user_id)
	club = Club.query.get_or_404(club_id)
	members = club.members
	form = create_club_minutes_form(club, purchase, fund)
	# form.purchaseform.entries = purchase
	# form.fundform.entries = fund
	if form.validate_on_submit():
            minute = Minutes(club_id=club_id, date=form.date.data, time=form.time.data, location=form.location.data, minute=form.notes.data)
            db.session.add(minute)
            for index, field in enumerate(form.attendance):
                attendance = Attendance(student_name=members[index].firstname + ' ' + members[index].lastname, present=form.attendance[index].data, minutes_id=minute.id)
                minute.attendance.append(attendance)	
            db.session.commit()
            flash('Minutes successfully recorded', 'success')
            return redirect(url_for('clubs.view_club_name', user_id=user.id))
	return render_template('record_minutes.html', title='Record', form=form, user=user, club=club, members=members)

@clubs.route("/view_minutes/<int:user_id>", methods=['GET', 'POST'])
@login_required
def view_club_name(user_id):
	user = User.query.get_or_404(user_id)
	# TODO: use the same form
	form = view_club_name_form(user)
	if form.validate_on_submit():
		# send user to the record_club_minutes
        	club = form.club_list.data
        	return redirect(url_for('clubs.view_minutes', user_id=user_id, club_id=club.id)) #clubs.view_minutes
	return render_template('view_clubs.html', title='View', form=form, user=user)

@clubs.route("/view_minutes/<int:user_id>/<int:club_id>", methods=['GET', 'POST'])
@login_required
def view_minutes(user_id, club_id):
	club = Club.query.get_or_404(club_id)
	user = User.query.get_or_404(user_id)
	minutes = club.minutes
	#if click "export" -->
		#return render_pdf(url_for('minutes_pdf', user_id=user_id, club_id=club_id))
	return render_template('view_minutes.html', title='View', user=user, club=club, minutes=minutes)

@clubs.route("/minutes_pdf/<int:user_id>/<int:club_id>/<int:minutes_id>.pdf", methods=['GET', 'POST'])
@login_required
def minutes_pdf(user_id, club_id, minutes_id):
	club = Club.query.get_or_404(club_id)
	user = User.query.get_or_404(user_id)
	minutes = Minutes.query.get_or_404(minutes_id) #GET THE Minutes for specific DAY
	return render_template('view_minutes_pdf.html', club=club, user=user, minutes=minutes)

@clubs.route("/schoolclubs", methods=['GET', 'POST'])
@login_required
def school_clubs():
    workbook = xlrd.open_workbook("/Users/joannafan/Desktop/clubsproject/clubsapp/clubs/portolaclubs.xlsx")
    worksheet = workbook.sheet_by_index(0)
    first_row=[]
    for col in range(worksheet.ncols):
        first_row.append(worksheet.cell_value(0,col))
    data = []
    for row in range(1, worksheet.nrows):
        record = {}
        for col in range(worksheet.ncols):
            if isinstance(worksheet.cell_value(row,col), str):
                if col==0:
                	club = worksheet.cell_value(row,col).strip()
                if col==1:
                    advisor = worksheet.cell_value(row,col).strip()
                if col==2:
                    room = worksheet.cell_value(row,col).strip()
            else:
                if col==0:
                	club = worksheet.cell_value(row,col).strip()
                if col==1:
                    advisor = worksheet.cell_value(row,col).strip()
                if col==2:
                    room = worksheet.cell_value(row,col).strip()
        post=Post(club=club, advisor=advisor, room=room)
        data.append(post)
    return render_template('schoolclubs.html', data=data)

# @clubs.route("/schoolclubs", methods=['GET', 'POST'])
# @login_required
# def school_clubs():
# 	df = pd.read_excel("/Users/joannafan/Desktop/clubsproject/clubsapp/clubs/portolaclubs.xlsx")
# 	# return render_template('schoolclubs.html', df=df)
# 	return df.to_html()