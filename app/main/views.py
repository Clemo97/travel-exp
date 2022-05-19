from . import main
from flask import render_template, request, redirect, url_for, abort

# # from ..models import User
# from auth.form import UpdateProfile, PitchForm
# from .. import db, photos


@main.route('/')
def index():
   


    return render_template('index.html')





@main.route('/recommend')
def recommend():
   


    return render_template('recommend.html')








