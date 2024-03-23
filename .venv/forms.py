# import necessary modules
from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, SelectField, SubmitField, SelectMultipleField
from wtforms.validators import DataRequired

class DataCollectionForm(FlaskForm):
    """
    create a form including name, student_number, email, grades, satisfaction, suggestion,facilities
    and feedback, DataRequired ensures the field is filled, no DataRequired for optional question
    """
    student_name = StringField('Name', validators=[DataRequired()])
    student_number = StringField('Student Number', validators=[DataRequired()])
    email = StringField('Email', validators=[DataRequired()])
    grades = TextAreaField('Grades Obtained in Courses', validators=[DataRequired()])
    satisfaction = SelectField('Overall Satisfaction', choices=[('very good', 'Very Good'), ('good', 'Good'), ('neither good nor bad', 'Neither Good nor Bad'), ('bad', 'Bad'), ('very bad', 'Very Bad')], validators=[DataRequired()])
    suggestion = TextAreaField('Suggestions for Improvement')
    facilities = SelectMultipleField('Facilities Ned be Improved', choices=[('screen projector', 'Screen Projector'), ('air conditioner', 'Air Conditioner'), ('heat', 'Heat'), ('ventilate system', 'Ventilate System'), ('radio', 'Radio'), ('desk/chair', 'Desk/Chair'), ('none', 'None')], validators=[DataRequired()])
    feedback = TextAreaField('Do you have other feedback?')
    # create a button to submit the form
    submit = SubmitField('Submit')