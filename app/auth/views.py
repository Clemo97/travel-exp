from flask import render_template, redirect, url_for,flash,request
from .form import RegistrationForm, LoginForm
from . import auth

# from .form import RegistrationForm,LoginForm

from flask_login import login_user, logout_user, login_required


@auth.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data.lower()).first()
        if user is not None and user.verify_password(form.password.data):
            login_user(user, form.remember_me.data)
            next = request.args.get('next')
            if next is None or not next.startswith('/'):
                next = url_for('main.index')
            return redirect(next)
        flash('Invalid email or password.')
    return render_template('auth/login.html', form=form)



@auth.route('/register', methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        user = User(email=form.email.data.lower(),
                    username=form.username.data,
                    password=form.password.data)
        db.session.add(user)
        db.session.commit()
        flash('You can now login.')
        return redirect(url_for('auth.login'))
    return render_template('auth/register.html', form=form)



# @auth.route('/login', methods=['GET','POST'])
# def login():
#     form = LoginForm()
#     if form.validate_on_submit():
#         if form.email.data == 'collo@gmail.com' and form.password.data == 'password':
#             flash('You have successfully logged in', 'success')
#             return redirect (url_for('main.index'))
#         else:
#             flash('Unsuccessful log in', 'danger')
#     return render_template('login.html', form=form)


# @auth.route('/register', methods=["GET","POST"])
# def register():
#     form = RegistrationForm()
#     if form.validate_on_submit():
#         flash(f'{ form.username.data} your account has been created', 'success')
#         return redirect(url_for('auth.login'))
    
#     return render_template('register.html', form=form)

