# python3 -m pipenv install flask flask-bcrypt pymysql
# python3 -m pipenv shell
# python3 server.py
from flask_app import app
from flask import render_template, redirect, request, session, flash
from flask_bcrypt import Bcrypt
from flask_app.models.user import User
from flask_app.models.recipe import Recipe

bcrypt = Bcrypt(app)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/register', methods=['POST'])
def register():
    if not User.validate_registration(request.form):
        return redirect('/')

    hashed_password = bcrypt.generate_password_hash(request.form['password'])

    data = {
        'first_name': request.form['first_name'],
        'last_name': request.form['last_name'],
        'email': request.form['email'],
        'password': hashed_password
    }

    session['user_id'] = User.save(data)
    print('////////////', session['user_id'])

    return redirect('/dashboard')


@app.route('/dashboard')
def dashboard():
    if 'user_id' not in session:
        return redirect('/')
    data = {
        'id': session['user_id']
    }
    logged_in_user = User.get_user_by_id(data)
    if logged_in_user == False:
        return redirect('/')
#######################
    recipes = Recipe.get_all()

    # print(ninjas.dojo_id)

    return render_template('dashboard.html', user=logged_in_user, recipes=recipes)


@app.route('/login', methods=['POST'])
def login():
    login_validation = User.validate_login(request.form)
    if not login_validation:
        return redirect('/')

    session['user_id'] = login_validation.id
    return redirect('/dashboard')


@app.route('/logout')
def logout():
    session.clear()
    return redirect('/')

###################################


@app.route('/recipes/<int:id>')
def view_recipe(id):

    get_selected = Recipe.get_one(id)
    return render_template('view.html', selected_recipe=get_selected)


@app.route('/recipes/edit/<int:id>')
# Displays current values as placeholders
def edit(id):
    get_selected = Recipe.get_one(id)

    return render_template('edit.html', selected_recipe=get_selected)


@app.route('/edit/<int:id>', methods=['POST'])
def edit_recipe_form(id):
    print(id)

    data = {
        'id': id,
        'name': request.form['name'],
        'description': request.form['description'],
        'instructions': request.form['instructions'],
        'date_made': request.form['date_made'],
        'under_thirty': request.form['under_thirty']

    }
    print('************************')
    print(data)
    Recipe.edit_one(data)
    return redirect('/recipes/%i' % id)
