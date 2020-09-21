from flask import render_template,request, redirect, url_for, abort
from . import main
from .forms import PitchForm
from ..models import Pitch
# Views
@main.route('/')
def index():
    '''
    View root page function that returns the index page and its data
    '''
    title = 'Home - Welcome to The best Pitching Website Online'

    
    search_pitch = request.args.get('pitch_query')
    

    return render_template('index.html', title = title)

@main.route('/pitch/new/', methods = ['GET','POST'])

def new_pitch():
    '''
    Function that creates new pitches
    '''
    form = PitchForm()


    if category is None:
        abort( 404 )

    if form.validate_on_submit():
        pitch= form.content.data
        category_id = form.category_id.data
        new_pitch= Pitch(pitch= pitch, category_id= category_id)

        new_pitch.save_pitch()
        return redirect(url_for('main.index'))

    return render_template('new_pitch.html', new_pitch_form= form, category= category)

@main.route('/category/<int:id>')
def category(id):
    '''
    function that returns pitches based on the entered category id
    '''
    category = PitchCategory.query.get(id)

    if category is None:
        abort(404)

    pitches_in_category = Pitches.get_pitch(id)
    return render_template('category.html' ,category= category, pitches= pitches_in_category)




