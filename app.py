from flask import Flask, render_template
from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, RadioField, SelectField, SubmitField
from wtforms.validators import DataRequired, Length, Email

app = Flask(__name__)
@app.route('/')
def index():
    return render_template('welcomepage.html')

@app.route('/info')
def info():
    return render_template('informationpage.html')

@app.route('/questionnaire')
def questionnaire():
    return render_template('datacollectionpage.html')

@app.route('/contact')
def contact():
    return render_template('contactpage.html')

class Surveyform(FlaskForm):
    name = StringField('Name', Validator=[DataRequired])
    student_number = StringField('Student number', validators=[DataRequired(), Length(min=7, max=7)])

if __name__ == '__main__':
   app.run(debug = True)