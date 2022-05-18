from . import main
from flask import render_template, request, redirect, url_for, abort
from flask_login import login_required
# # from ..models import User
# from auth.form import UpdateProfile, PitchForm
# from .. import db, photos


@main.route('/')
def index():
   


    return render_template('index.html')



@main.route('/user')
def profile():
 
    return render_template()

@main.route('/user/update', methods=["GET","POST"])
@login_required
def update_profile():
    

        
    return render_template('profile.html')









