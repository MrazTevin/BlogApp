from flask import render_template
from app import app


@app.route('/')
def index():

    '''
    will return the index page and its data
    '''
    return render_template('index.html')
