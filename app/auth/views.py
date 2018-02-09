from flask import render_template
from . import auth
#from app import app


@auth.route('/login')
def login():

    '''
    will return the index page and its data
    '''
    return render_template('auth/login.html')
