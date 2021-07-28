import petpy
import os
from flask_app import app
from flask import render_template, redirect, request, session, flash


class Petfinder:
    
    def __init__(self, data):
        self.key = data['key']
        self.secret = data['secret']


    
    
    @classmethod
    def get_access(cls):
        key = os.getenv('PETFINDER_KEY'),
        secret = os.getenv('PETFINDER_SECRET_KEY')
        
        pf = petpy.Petfinder(key=key, secret=secret)

        return pf


    @classmethod
    def first_20(cls):
        animals = pf.animals()
        return animals

    @classmethod
    def get_type(type):
        pets = pf.animal_types(type)
        # print('PPPPPP', pf),
        print('PPPPPP', pets)

        return pets

    @classmethod
    def get_breeds(cls):
        animal_breeds = pf.breeds()
        print('PPPPPP', animal_breeds)

        for breed in animal_breeds['breeds']:
            print(breed)
            print(animal_breeds['breeds'][breed][0:3])
            return animal_breeds

pf = Petfinder.get_access()
