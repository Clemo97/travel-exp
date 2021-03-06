from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField, TextAreaField, DateTimeField, FileField
from wtforms.validators import DataRequired, EqualTo, Length,Email



class RegistrationForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired(), Length(min=2, max=10)])
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    repeat_password = PasswordField('Repeat Password', validators=[DataRequired(), EqualTo('password')])

    submit = SubmitField('Sign-Up')


class LoginForm(FlaskForm):
    email = StringField('Email', validators=[DataRequired(), Email()])

    password = PasswordField('Password', validators=[DataRequired()])
    remember = BooleanField("Remember Me")

    submit = SubmitField('Login')    