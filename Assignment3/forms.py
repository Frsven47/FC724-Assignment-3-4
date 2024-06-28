from flask_wtf import FlaskForm
from wtforms import StringField, RadioField, SubmitField
from wtforms.validators import DataRequired

class QuestionnaireForm(FlaskForm):
    short_term_goal = StringField('Short-term Goal', validators=[DataRequired()])
    long_term_goal = StringField('Long-term Goal', validators=[DataRequired()])
    multiple_choice = RadioField('Multiple Choice', choices=[('option1', 'Option 1'), ('option2', 'Option 2'), ('option3', 'Option 3')], validators=[DataRequired()])
    submit = SubmitField('Submit')
