# python3 -m pipenv install flask pymysql
# python3 -m pipenv shell
# python3 server.py
from flask import Flask, render_template, request, redirect, session
# Import the class itself
from friend import Friend

# Create a new instance of the Flask class called 'app'
app = Flask(__name__)


@app.route('/')
def index():
    return render_template("index.html")


@app.route('/allfriends')
def all_friends():

    friends = Friend.get_all()

    return render_template('index.html', friends=friends)


@app.route('/create', methods=['POST'])
def create_friend():
    data = {
        'first_name': request.form['first_name'],
        'last_name': request.form['last_name'],
        'occupation': request.form['occupation']
    }

    Friend.save(data)
    # NEVER RENDER ON A POST
    return redirect('/')


if __name__ == '__main__':   # Ensure this file is being run directly and not from a different module
    app.run(debug=True)    # Run the app in debug mode.
