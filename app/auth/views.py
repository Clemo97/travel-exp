from flask import render_template, redirect, url_for,flash,request
from . import auth

# from .form import RegistrationForm,LoginForm

from flask_login import login_user, logout_user, login_required

@auth.route('/login', methods=['GET','POST'])
def login():
   
   
 return render_template('login.html')


@auth.route('/register', methods=["GET","POST"])
def register():
    
     
    
    return render_template('register.html')
