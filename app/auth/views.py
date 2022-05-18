from flask import render_template, redirect, url_for,flash,request
from form import RegistrationForm, LoginForm
from . import auth

# from .form import RegistrationForm,LoginForm

from flask_login import login_user, logout_user, login_required

@auth.route('/login', methods=['GET','POST'])
def login():
    form = LoginForm()
   
   
    return render_template('login.html', form=form)


@auth.route('/register', methods=["GET","POST"])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        flash(f'{ form.username.data} your account has been created', 'success')
        return redirect(url_for('login'))
    
    return render_template('register.html', form=form)

