# import modules from flask and form template from forms.py
from flask import Flask, render_template, redirect, url_for, request
from forms import DataCollectionForm

# initialize the Flask application
app = Flask(__name__)
# create a secret key for the application
app.config['SECRET_KEY'] = '123'

# define the route of welcome page
@app.route('/')
def welcome_page():
    # render the template of welcome page
    return render_template('WelcomePage.html')

# define the route of welcome page
@app.route('/information')
def information_page():
    # render the template of information page
    return render_template('InformationPage.html')

# define the route of data collection page, create GET,POST methods
@app.route('/data_collection', methods=['GET', 'POST'])
def data_collection_page():
    # instantiate the form
    form = DataCollectionForm()
    if request.method == 'POST':
        # check if the form is successfully submitted
        if form.validate_on_submit():
            # open or create the data.txt file in append mode
            with open('data.txt', 'a') as f:
                # write student data in the file
                f.write(f"Name: {form.student_name.data}, Student Number: {form.student_number.data}, Email: {form.email.data}, Grades: {form.grades.data}, Satisfaction: {form.satisfaction.data}, Facilities: {form.facilities.data}, Feedback: {form.feedback.data}\n")
            # redirect to the welcome page
            return redirect(url_for('welcome_page'))
    # if submit or validation failed, render the template of data collection page and form
    return render_template('DataCollectionPage.html', form=form)

if __name__ == '__main__':
    # run the Flask app with debug
    app.run(debug=True)
