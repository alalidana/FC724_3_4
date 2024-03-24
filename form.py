from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, RadioField, SelectField, SubmitField
from wtforms.validators import DataRequired, Length, Email, NumberRange
class Surveyform(FlaskForm):
    name = StringField('Name', Validator=[DataRequired()], for="name")
    student_number = StringField('Student number', validators=[DataRequired()], id="student_number", Length(min=7, max=7), message='Student number must be P followed by 6 digits.'])
    email = StringField('Email', Validator=[DataRequired, Email()])
    attendance = StringField('Attendance rate', validators=[DataRequired()], NumberRange(min=0, max=100))
    students = StringField('Total number of students in Class', validators=[DataRequired()])
    self_learning = RadioField('Hours Spent on Self-Learning', choices=[('1-2', '1-2 hours'),
                                                                        ('3-4', '3-4 hours'), ('5-6', '5-6 hours'), ('7+', '7+ hours')])
    performance = SelectField('Academic Performance', choices=[('1', '1'), ('2', '2'), ('3', '3'), ('4', '4'),
                                                               ('5', '5'), ('6', '6'), ('7', '7'), ('8', '8'), ('9', '9'), ('10', '10')])
    challenging_courses = TextAreaField('Challenging Courses')
    resources_satisfaction = SelectField('Resource Satisfaction Level', choices=[('1', '1'), ('2', '2'), ('3', '3'), ('4', '4'),
                                                               ('5', '5'), ('6', '6'), ('7', '7'), ('8', '8'),
                                                               ('9', '9'), ('10', '10')])
    improvement_suggestions = TextAreaField('Improvement Suggestions')
    goals = TextAreaField('Goals')
    submit = SubmitField('Submit')