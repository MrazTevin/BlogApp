from flask import render_template,redirect,request,request,url_for,flash
from flask_login import login_user, logout_user, login_required
from .forms import LoginForm
from ..models import User
from . import auth
from .. import db


#from app import app


@auth.route('/login')
def login():
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if user is not None and user_verify_password(form.password.data):
            login_user(user, form.remember_me.data)
            return redirect(request.args.get('next')) or url_for('main.index')
        flash('Invalid username or password')
    return render_template('auth/login.html', form=form)


@auth.route('/logout')
def logout():
    logout_user()
    flash('You have been logged out.')
    return redirect(url_for('main.index'))


@auth.route('/register', methods=["GET", "POST"])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        user = User(email = form.email.data, username = form.username.data,password = form.password.data)
        db.session.add(user)
        db.session.commit()
        return redirect(url_for('auth.login'))
        title = "New Account"
    return render_template('auth/register.html',registration_form = form)
