from flask import render_template
from flask_login import login_user
from .forms import LoginForm
from . import auth


#from app import app


@auth.route('/login')
def login():

    '''
    will return the index page and its data
    '''
    return render_template('auth/login.html')
