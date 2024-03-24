from flask import Flask, render_template
from form import Surveyform

app = Flask(__name__)
app.config['SECRET_KEY'] = 'speak-up'
@app.route('/')
def index():
    return render_template('welcomepage.html')

@app.route('/info')
def info():
    return render_template('informationpage.html')

@app.route('/questionnaire', methods=['GET', 'POST'])
def questionnaire():
    #initializing form
    form= Surveyform()
    #check if form is submit and valid
    if form.validate_on_submit():
        #opens the file in append mode and write form data
        with open('form_responses.txt', 'a') as file:
            file.write(f"Name: {form.name.data}\n")
    return render_template('datacollectionpage.html', form= form)

@app.route('/contact')
def contact():
    return render_template('contactpage.html')

if __name__ == '__main__':
   app.run(debug = True)