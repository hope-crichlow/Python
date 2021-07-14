# python3 -m pipenv install flask jinja2
# python3 -m pipenv shell
# python3 server.py
from flask import Flask, render_template, request, redirect, session
# Create a new instance of the Flask class called 'app'
app = Flask(__name__)
# set a secret key for security purposes
app.secret_key = 'keep it secret, keep it safe'


@app.route('/')
def index():
    return render_template("index.html")


@app.route('/process', methods=['POST'])
def process_result():
    print("Got Post Info")
    print(request.form['name'])

    session['name'] = request.form['name']
    session['location'] = request.form['location']
    session['language'] = request.form['language']
    session['comment'] = request.form['comment']
    return redirect('/result')


@app.route('/result')
def show_result():
    print("Showing Info From the Form")

    return render_template('result.html')


if __name__ == '__main__':   # Ensure this file is being run directly and not from a different module
    app.run(debug=True)    # Run the app in debug mode.
