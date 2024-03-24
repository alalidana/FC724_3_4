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
    email = StringField('Email', Validator=[DataRequired, Email()])
    attendance = StringField('Attendance rate', validators=[DataRequired()])
    students = StringField('Total number of students in Class', validators=[DataRequired()])
    self_learning = RadioField('Hours Spent on Self-Learning', choices=[('1-2', '1-2 hours'),
                                                                        ('3-4', '3-4 hours'), ('5-6', '5-6 hours'), ('7+', '7+ hours')])
    performance = SelectField('Academic Performance', choices=[('1', '1'), ('2', '2'), ('3', '3'), ('4', '4'),
                                                               ('5', '5'), ('6', '6'), ('7', '7'), ('8', '8'), ('9', '9'), ('10', '10')])
if __name__ == '__main__':
   app.run(debug = True)