from flask import Flask, render_template

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

if __name__ == '__main__':
   app.run(debug = True)