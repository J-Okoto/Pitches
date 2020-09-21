from flask import render_template,request, redirect, url_for, abort
from . import main

# Views
@main.route('/')
def index():
    '''
    View root page function that returns the index page and its data
    '''
    title = 'Home - Welcome to The best Pitching Website Online'

    
    search_pitch = request.args.get('pitch_query')
    

    return render_template('index.html', title = title)



