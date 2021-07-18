from flask import Flask, render_template, request, redirect, session
# Import the class itself
from user import User
# Create a new instance of the Flask class called 'app'
app = Flask(__name__)


@app.route('/')
def index():
    users = User.get_all()

    return render_template('index.html', users=users)


@app.route('/users')
def all_users():

    users = User.get_all()

    return render_template('index.html', users=users)


@app.route('/users/new')
def new_user():

    return render_template('new_user.html')


@app.route('/create', methods=['POST'])
def create_user():
    data = {
        'first_name': request.form['first_name'],
        'last_name': request.form['last_name'],
        'email': request.form['email']
    }

    User.save(data)
    # NEVER RENDER ON A POST
    return redirect('/users')


if __name__ == '__main__':   # Ensure this file is being run directly and not from a different module
    app.run(debug=True)    # Run the app in debug mode.