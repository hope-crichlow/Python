# python3 -m pipenv install flask flask-bcrypt pymysql
# python3 -m pipenv shell
# python3 server.py
from flask_app import app
from flask import render_template, redirect, request, session, flash
from flask_bcrypt import Bcrypt
from flask_app.models.user import User
from flask_app.models.band import Band

bcrypt = Bcrypt(app)


@app.route('/')
def index():
    return render_template('index.html')


# @app.route('/dashboard')
# def dashboard():
#     return render_template('dashboard.html')


@app.route('/dashboard')
def bands():
    if 'user_id' not in session:
        return redirect('/')
    data = {
        'id': session['user_id']
    }
    logged_in_user = User.get_user_by_id(data)
    if logged_in_user == False:
        return redirect('/')
#######################
    results = Band.get_all_bands()
    print('********DATA RETURNED FROM DATABASE**********')
    print(results)
    bands = []

    for band in results:
        print('***********************')
        print(band.band_name, '\n', band.founding_member, '\n', band.genre)
        bands.append(band)
        print('***********************')

    return render_template('dashboard.html', logged_user=logged_in_user, bands=bands)



@app.route('/register', methods=['POST'])
def register():
    registration_validation = User.validate_registration(request.form)
    if not registration_validation:
        return redirect('/')

    hashed_password = bcrypt.generate_password_hash(request.form['password'])

    data = {
        'first_name': request.form['first_name'],
        'last_name': request.form['last_name'],
        'email': request.form['email'],
        'password': hashed_password
    }
    session['first_name'] = request.form['first_name']
    session['last_name'] = request.form['last_name']
    session['email'] = request.form['email']
    
    current_user = registration_validation
    print('//////////CURRENT USER >>>>>>', current_user)
    
    # session['user_id'] = User.save(data)
    current_user = User.save(data)
    print('////////////', session['user_id'], session['first_name'])
    
    # session['user_id'] = current_user[id]
    session['first_name'] = current_user.first_name
    print('//////////CURRENT USER >>>>>>', current_user.first_name)


    return redirect('/dashboard')


@app.route('/login', methods=['POST'])
def login():
    login_validation = User.validate_login(request.form)
    if not login_validation:
        return redirect('/')

    current_user = login_validation
    print('//////////', current_user)
    session['user_first_name'] = current_user.first_name
    session['user_id'] = current_user.id
    print('//////////', session['user_first_name'])

    return redirect('/dashboard')


@app.route('/logout')
def logout():
    session.clear()
    return redirect('/')

