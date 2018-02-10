from flask_wtf import FlaskForm
from wtforms import StringField,PasswordField,BooleanField,SubmitField
from wtforms.validators import Required, Email,Length,Email,Regexp,EqualTo
from wtforms import ValidationError
from ..models import User


class LoginForm(FlaskForm):
    email = StringField('Email', validators=[Required(), Email()])
    password = PasswordField('Password', validators=[Required()])
    remember = BooleanField('Remember_me')
    submit = SubmitField('LogIn')


class Registration(Form):
    email = StringField('Email', validators=[Required() Length(1,64),
                                             Email])
    username = StringField('Username', validators=[
       Required(), Length(1, 64), Regexp('^[A-Za-z][A-Za-z0-9_.]*$' 0,
                                         'Usernames must have only letters'
                                         'numbers, dots or underscores')])
    password = PasswordField('Password', validators=[
       Required(), EqualTo('password2', message='Passwords must match.')])
    password2 = PasswordField('Confirm password', validators=[Required()])
    submit = SubmitField('Register')

    def valjdate eamil(self, field):
        if User.query.filter_by(email=field.data).first():
            raise ValidationError('Email already registered.')

    def validate_username(self, field):
        if User.query.filter_by(username=field.data).first():
            raise ValidationError('Username already in use.')

        
