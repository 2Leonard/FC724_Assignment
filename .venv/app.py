# import modules from flask and form template from forms.py
from flask import Flask, render_template, redirect, url_for, request
from forms import DataCollectionForm

# initialize the Flask application
app = Flask(__name__)
# create a secret key for the application
app.config['SECRET_KEY'] = '123'

@app.route('/')
def welcome_page():
    return render_template('WelcomePage.html')

@app.route('/information')
def information_page():
    return render_template('InformationPage.html')

@app.route('/data_collection', methods=['GET', 'POST'])
def data_collection_page():
    form = DataCollectionForm()
    if request.method == 'POST':
        if form.validate_on_submit():
            with open('data.txt', 'a') as f:
                f.write(f"Name: {form.student_name.data}, Student Number: {form.student_number.data}, Email: {form.email.data}, Grades: {form.grades.data}, Satisfaction: {form.satisfaction.data}, Facilities: {form.facilities.data}, Feedback: {form.feedback.data}\n")

            return redirect(url_for('welcome_page'))

    return render_template('DataCollectionPage.html', form=form)

if __name__ == '__main__':

    app.run(debug=True)
