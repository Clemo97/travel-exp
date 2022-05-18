from . import main
from flask import render_template, request, redirect, url_for, abort
from flask_login import login_required
# # from ..models import User
# from auth.form import UpdateProfile, PitchForm
# from .. import db, photos


@main.route('/')
def index():
   


    return render_template()



@main.route('/user/<>')
def profile():
 
    return render_template()

@main.route('/user/<>/update', methods=["GET","POST"])
@login_required
def update_profile():
    

        
    return render_template('profile/update.html')

@main.route('/user/<>/update/pic', methods=["POST"])
@login_required
def update_pic():
   
    return redirect(url_for('main.profile'))

@main.route('/new/pitch', methods=["GET","POST"])
@login_required
def new_pitch():
    

    return render_template('pitch/new_pitch.html')






