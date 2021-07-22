from flask_app import app
from flask import render_template, redirect, request, session, flash
from flask_app.models.ninja import Ninja
from flask_app.models.dojo import Dojo


@app.route('/')
def index():

    return redirect('/dojos')


@app.route('/ninjas')
def new_ninja():
    dojos = Dojo.get_all()
    return render_template('new_ninja.html', dojos=dojos)


@app.route('/create', methods=['POST'])
def create_ninja():
    associated_dojo_url = "/dojos/" + request.form['dojo_id']
    data = {
        'dojo_id': request.form['dojo_id'],
        'first_name': request.form['first_name'],
        'last_name': request.form['last_name'],
        'age': request.form['age']
    }

    print('****************')
    print(data)
    Ninja.save_ninja(data)
    
    # NEVER RENDER ON A POST
    return redirect('/')
