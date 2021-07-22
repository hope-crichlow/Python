from flask_app import app
from flask import render_template, redirect, request, session, flash
from flask_app.models.dojo import Dojo
# import flask_app.models.dojo import Dojo
from flask_app.models.ninja import Ninja


# @app.route('/')
# def index():

#     return redirect('/dojos')


@app.route('/dojos')
def all_dojos():

    dojos = Dojo.get_all()

    return render_template('index.html', dojos=dojos)


@app.route('/create_dojo', methods=['POST'])
def create_dojo():
    data = {
        'name': request.form['name']
    }
    print(data)
    Dojo.save_dojo(data)
    # NEVER RENDER ON A POST
    return redirect('/')


@app.route('/dojos/<int:dojo_id>')
def show_ninjas(dojo_id):
    get_selected = Dojo.get_one(dojo_id)

    ninjas = Ninja.get_all_ninjas_from_dojo(dojo_id)
    # print(ninjas.dojo_id)

    return render_template('show_dojo.html', ninjas=ninjas, selected_dojo=get_selected)
