
from flask import Blueprint, render_template, url_for, redirect, request, flash
from flask_login import current_user, login_required
from clubsapp import db
from clubsapp.models import Club
# from clubsapp.clubs.forms import RegisterClubForm


clubs = Blueprint('clubs', __name__)
