from flask import Flask, render_template, flash
from form import Surveyform

app = Flask(__name__)
app.config['SECRET_KEY'] = 'speak-up'
#define flask route for welcomepage
@app.route('/')
def index():
    return render_template('welcomepage.html')
#define flask route for informationpage
@app.route('/info')
def info():
    return render_template('informationpage.html')
#define flask route for questionaire
@app.route('/questionnaire', methods=['GET', 'POST'])
def questionnaire():
    #initializing form
    form= Surveyform()
    #check if form is submit and valid
    if form.validate_on_submit():
        #read existing student numbers to check for duplicates
        existing_student_numbers = set()
        try:
            with open('form_responses.txt', 'r') as file:
                for line in file:
                    if line.startswith("Student Number: "):
                        existing_student_numbers.add(line.strip().split(": ")[1])
        except FileNotFoundError:
            # This means the file does not exist yet, so no submissions have been made.
            pass
        #opens the file in append mode and write form data
        with open('form_responses.txt', 'a') as file:
            file.write(f"Name: {form.name.data}\n")
            file.write(f"Student Number: {form.student_number.data}\n")
            file.write(f"Email: {form.email.data}\n")
            file.write(f"Attendance Rate: {form.attendance.data}\n")
            file.write(f"Number of Students: {form.students_number.data}\n")
            file.write(f"Self Learning Hours: {form.self_learning.data}\n")
            file.write(f"Academic Performance: {form.performance.data}\n")
            file.write(f"Challenging Courses: {form.challenging_courses.data}\n")
            file.write(f"Teaching Methods Satisfaction: {form.teaching_methods.data}\n")
            file.write(f"Resources Satisfaction: {form.resources_satisfaction.data}\n")
            file.write(f"Improvement Suggestions: {form.improvement_suggestions.data}\n")
            file.write(f"Goals being met opinion: {form.goals.data}\n")
            file.write("------------------------------------------------\n")
        #flash system to display feedback to the user.
        flash('Your survey response has been successfully submitted!', 'success')
    return render_template('datacollectionpage.html', form= form)

#define flask route for contactpage
@app.route('/contact')
def contact():
    return render_template('contactpage.html')

if __name__ == '__main__':
   app.run(debug = True)