from flask import render_template,request, redirect, url_for, abort
from app import app

# Views
@app.route('/')
def index():
    '''
    View root page function that returns the index page and its data
    '''
    title = 'Home - Welcome to The best Pitching Website Online'

    

    return render_template('index.html', title = title)



