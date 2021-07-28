# from ajax.ajax_flask.puppy_play_date.flask_app.models.pf import get_access
# import requests
# from flask_app.models.pet import User
from flask_app import app
from flask import render_template, jsonify, request, redirect
# import os
# import petpy
from flask_app.models.pf import Petfinder

pf = Petfinder.get_access()


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/types')
def get_animal_types():

    animal_types = pf.animal_types()
    print(animal_types)
    print('************Animal Types***********')
    for animal in animal_types['types']:
        print('***********************')
        print(animal['name'], '\n', animal['coats'])
        print('***********************')
    return render_template('index.html')


@app.route('/animals')
def get_animals():
    fluff = Petfinder.first_20()
    print(fluff)
    for animals in fluff['animals']:
        print('***********************')
        print(animals['name'], '\n', animals['type'],'\n', animals['breeds'])
        print('**********************')
    # animal_types = pf.animal_types()
    # print(animal_types)
    # for animal in animal_types['types']:

    #     print(animal['name'], '\n', animal['coats'])

    return render_template('index.html')

@app.route('/dogs')
def all_dogs():
    
    dog_type= pf.animal_types('dog')
    print('***********************')
    print('DOGGGGGGGSSSSS', dog_type)

    # for dogs in dog_type['type']:
    #     print('**********DOGS*************')
    #     print(dogs['coats'],'\n', dogs['colors'])

    return render_template('view_dogs.html')



@app.route('/breeds')
def all_breeds():
    animal_breeds= Petfinder.get_breeds()
    for breed in animal_breeds['breeds']:
        print(breed)
        #Only prints out first 3
        print(animal_breeds['breeds'][breed][0:3])
    return render_template('view_dogs.html')


# @app.route('/dogs')
# def all_dogs():
#     pf = Petfinder.get_access()
#     pass

