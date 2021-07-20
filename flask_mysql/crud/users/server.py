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


@app.route('/users/<int:user_id>')
def show_user(user_id):

    get_selected = User.get_one(user_id)
    print(get_selected.first_name)

    return render_template('show_one.html', selected_user=get_selected)


@app.route('/users/<int:user_id>/edit')
# Displays current values as placeholders
def edit(user_id):
    get_selected = User.get_one(user_id)
    # print(get_selected.first_name)
    # edit_user_form(user_id)
    return render_template('edit_user.html', selected_user=get_selected)


@app.route('/edit/<int:user_id>', methods=['POST'])
def edit_user_form(user_id):
    print(user_id)

    # selected_user.user_id == user_id
    data = {
        'user_id': user_id,
        'first_name': request.form['first_name'],
        'last_name': request.form['last_name'],
        'email': request.form['email']
    }
    print('************************')

    print(data)
    User.edit_one(data)
    return redirect('/')


if __name__ == '__main__':   # Ensure this file is being run directly and not from a different module
    app.run(debug=True)    # Run the app in debug mode.
