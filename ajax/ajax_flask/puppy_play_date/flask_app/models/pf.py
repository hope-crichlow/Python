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
        
        
        results = pf
        print('000000000', results)
        return results
