# from ajax.ajax_flask.puppy_play_date.flask_app.models.pf import get_access
import requests
from flask_app.models.pet import User
from flask_app import app
from flask import render_template, jsonify, request, redirect


import os
import petpy
from flask_app.models.pf import Petfinder

print('//////////////', os.environ.get("FLASK_APP_API_KEY"))


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/animals')
def get_pets():
    pf = Petfinder.get_access()
    
    animal_types = pf.animal_types()
    types =jsonify(animal_types)
    print('3333333333',types)
    for animal in animal_types['types']:
        print(animal['name'], '\n', animal['coats'])
    return render_template('index.html')
