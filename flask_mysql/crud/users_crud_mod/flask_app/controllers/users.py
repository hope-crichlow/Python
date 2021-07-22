from flask_app import app
from flask import render_template, redirect, request, session, flash
import flask_app.models.user import User

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

    return render_template('edit_user.html', selected_user=get_selected)


@app.route('/edit/<int:user_id>', methods=['POST'])
def edit_user_form(user_id):
    print(user_id)

    data = {
        'user_id': user_id,
        'first_name': request.form['first_name'],
        'last_name': request.form['last_name'],
        'email': request.form['email']
    }
    print('************************')
    user_id = user_id
    print(data)
    User.edit_one(data)
    return redirect('/users/%i' % user_id)


@app.route('/delete/<int:user_id>')
def delete_user(user_id):
    data = {
        'user_id': user_id
    }
    User.delete_one(data)

    return redirect('/users')
