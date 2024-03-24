from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, RadioField, SelectField, SubmitField
from wtforms.validators import DataRequired, Length, Email, NumberRange
class Surveyform(FlaskForm):
    name = StringField('Name: ', validators=[DataRequired()], render_kw={'placeholder': 'Enter your name', 'id': 'name'})

    student_number = StringField('Student number: ', validators=[DataRequired(), Length(min=7, max=7,message='Student number must be P followed by 6 digits.')],
                                 render_kw={'placeholder': 'P######', 'id': 'student_number'})

    email = StringField('Email: ', validators=[DataRequired(), Email()],render_kw={'placeholder': 'example@example.com', 'id': 'email'})

    attendance = StringField('What is your average class attendance rate?', validators=[DataRequired(), NumberRange(min=0, max=100)],render_kw={'placeholder': 'Enter percentage', 'id': 'attendance'})

    students_number = StringField('What is the total number of students in your class?', validators=[DataRequired()],render_kw={'placeholder': 'Enter total number', 'id': 'students'})

    self_learning = RadioField('Hours Spent on Self-Learning',choices=[('1-2', '1-2 hours'), ('3-4', '3-4 hours'), ('5-6', '5-6 hours'),
                                        ('7+', '7+ hours')], validators=[DataRequired()])

    performance = SelectField('Academic Performance',choices=[('Select...', 'Select...'), ('1', '1'),('2', '2'), ('3', '3'), ('4', '4'), ('5', '5'), ('6', '6'),
                                       ('7', '7'), ('8', '8'), ('9', '9'), ('10', '10')], validators=[DataRequired()])

    challenging_courses = TextAreaField('Which courses have you found most challenging and why?', validators=[DataRequired()],
                                        render_kw={'placeholder': 'Describe here', 'id': 'challengingCourses'})

    teaching_methods= TextAreaField('Are you satisfied with the teaching methods used in the classes? Explain why or why not.', validators=[DataRequired()],
                                        render_kw={'placeholder': 'Describe here', 'id': 'teaching_methods'})

    resources_satisfaction = SelectField('Resource Satisfaction Level',
                                         choices=[('Select...', 'Select...'), ('1', '1'), ('2', '2'), ('3', '3'), ('4', '4'), ('5', '5'),
                                                  ('6', '6'), ('7', '7'), ('8', '8'), ('9', '9'), ('10', '10')],
                                         validators=[DataRequired()])

    improvement_suggestions = TextAreaField('Can you provide recommendations on how we can improve the academic experience at GIC?', validators=[DataRequired()],
                                            render_kw={'placeholder': 'Your recommendations', 'id': 'improvement'})

    goals = TextAreaField('Do you feel your academic goals are being met at GIC? Why or why not?', validators=[DataRequired()],
                          render_kw={'placeholder': 'Your academic goals', 'id': 'goals'})

    submit = SubmitField('Submit')