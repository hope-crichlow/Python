# python3 -m pipenv install flask flask-bcrypt pymysql
# python3 -m pipenv shell
# python3 server.py
from flask_app import app
from flask import render_template, redirect, request, session, flash
from flask_bcrypt import Bcrypt
from flask_app.models.user import User
from flask_app.models.painting import Painting




@app.route('/paintings/new')
def new_painting():
    if 'user_id' not in session:
        return redirect('/')
# get_selected = Painting.get_one(id)
    return render_template('new.html')

@app.route('/create', methods=['POST'])
def create_painting():
    painting_validation = Painting.validate_new_painting(request.form)
    if painting_validation == False:
        return redirect('/paintings/new')
    else:
        data = {
            "user_id": session['user_id'],
            "title": request.form['title'],
            "description": request.form['description'],
            'price': request.form['price']
        }


    print('****************')
    print(data)
    Painting.save_painting(data)
    
    # NEVER RENDER ON A POST
    return redirect('/dashboard')


@app.route('/paintings/<int:id>')
def view_painting(id):
    
    data = {
        'id': id
    }
    artist = User.get_user_by_id(data)

    
    print('///////////**********',artist.first_name)

    get_selected = Painting.get_one(id)
    return render_template('view.html', selected_painting=get_selected, artist=artist)


@app.route('/paintings/edit/<int:id>')
# Displays current values as placeholders
def edit(id):
    get_selected = Painting.get_one(id)

    return render_template('edit.html', selected_painting=get_selected)


@app.route('/<int:id>/edit', methods=['POST'])
def edit_painting_form(id):
    print(id)

    data = {
        'id': id,
        'title': request.form['title'],
        'description': request.form['description'],
        'price': request.form['price'],
    }
    print('************************')
    print(data)
    Painting.edit_one(data)
    return redirect('/paintings/%i' % id)


