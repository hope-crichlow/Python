# python3 -m pipenv install flask flask-bcrypt pymysql
# python3 -m pipenv shell
# python3 server.py
from flask_app import app
from flask import render_template, redirect, request, session, flash
from flask_bcrypt import Bcrypt
from flask_app.models.user import User
from flask_app.models.painting import Painting

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
    print('////////////', session['user_id'], session['user_name'])

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
    paintings = Painting.get_all_paintings()

  
    return render_template('dashboard.html', logged_user=logged_in_user, paintings=paintings)


@app.route('/login', methods=['POST'])
def login():
    login_validation = User.validate_login(request.form)
    if not login_validation:
        return redirect('/')

    # session['user_id'] = login_validation.id
    curreent_user = login_validation
    print('//////////', curreent_user)
    session['user_first_name']= curreent_user.first_name
    # print('//////////', session['user_first_name'])

    return redirect('/dashboard')


@app.route('/logout')
def logout():
    session.clear()
    return redirect('/')

###################################

@app.route('/paintings/new')
def new_painting():

# get_selected = Painting.get_one(id)
    return render_template('new.html')

@app.route('/create', methods=['POST'])
def create_painting():
 
    data = {
        'dojo_id': request.form['dojo_id'],
        'first_name': request.form['first_name'],
        'last_name': request.form['last_name'],
        'age': request.form['age']
    }

    print('****************')
    print(data)
    painting.save_painting(data)
    
    # NEVER RENDER ON A POST
    return redirect('/')


@app.route('/paintings/<int:id>')
def view_painting(id):

    get_selected = Painting.get_one(id)
    return render_template('view.html', selected_painting=get_selected)


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
