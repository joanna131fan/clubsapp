import pandas as pd
from flask import Blueprint, render_template, url_for, redirect, request, flash
from flask_login import current_user, login_required
from clubsapp import db
from clubsapp.utils import ROLES
from clubsapp.models import Club, User, Minutes, Attendance, Post
from clubsapp.main.forms import select_school, schools
import xlrd

main = Blueprint('main', __name__)


@main.route("/home")
@login_required
def home():
	news = ['ClubsApp is Constantly Being Updated'] #enter into excel
	return render_template('home.html', title='Home', news=news)


@main.route("/about")
@login_required
def about():
	return render_template('about.html', title='About')
# TODO: select schools
# @main.route("/schools", methods=['GET', 'POST'])
# @login_required
# def school():
# 	form = select_school()
# 	if form.validate_on_submit():
# 		return redirect(url_for('main.schoolclubs', id=int(form.school.data)))
# 	return render_template('schoolselect.html', form=form)

@main.route("/schoolclubs", methods=['GET'])
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
                if col==3:
                    contact = worksheet.cell_value(row,col).strip()
            else:
                if col==0:
                	club = worksheet.cell_value(row,col).strip()
                if col==1:
                    advisor = worksheet.cell_value(row,col).strip()
                if col==2:
                    room = worksheet.cell_value(row,col).strip()
                if col==3:
                    contact = worksheet.cell_value(row,col).strip()
        post=Post(club=club, advisor=advisor, room=room, contact=contact)
        data.append(post)
    return render_template('schoolclubs.html', data=data)