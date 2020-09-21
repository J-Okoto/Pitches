from flask_wtf import FlaskForm
from wtforms import StringField,TextAreaField,SubmitField, SelectField, RadioField
from wtforms.validators import Required


class PitchForm(FlaskForm):
    category_id = SelectField('Select Category', choices=[('1', 'Interview'), ('2', 'Pick Up Lines'), ('3', 'Promotion'),('4','Product')])
    content = TextAreaField('YOUR PITCH')
    submit = SubmitField('Create Pitch')

class CommentsForm(FlaskForm):
    comment = TextAreaField('Comment', validators=[Required()])
    vote=RadioField('default field arguments', choices=[('1', 'UpVote'), ('1', 'DownVote')])
    submit = SubmitField('SUBMIT')  
