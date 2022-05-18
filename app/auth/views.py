from flask import render_template, redirect, url_for,flash,request
from . import auth
from ..models import User
from .form import RegistrationForm,LoginForm
from  .. import db 
from flask_login import login_user, logout_user, login_required

@auth.route('/login', methods=['GET','POST'])
def login():
   
   
 return render_template('auth/login.html')


@auth.route('/register', methods=["GET","POST"])
def register():
    
     
    
    return render_template('/auth/register.html')

