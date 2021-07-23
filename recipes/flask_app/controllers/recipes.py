# python3 -m pipenv install flask flask-bcrypt pymysql
# python3 -m pipenv shell
# python3 server.py
from flask_app import app
from flask import render_template, redirect, request, session, flash
from flask_bcrypt import Bcrypt
from flask_app.models.user import User


@app.route('/')
def index():
    return render_template('index.html')




# @app.route('/dashboard')
# def show_ninjas(dojo_id):
#     get_selected = Dojo.get_one(dojo_id)

#     ninjas = Ninja.get_all_ninjas_from_dojo(dojo_id)
#     # print(ninjas.dojo_id)

#     return render_template('show_dojo.html', ninjas=ninjas, selected_dojo=get_selected)
