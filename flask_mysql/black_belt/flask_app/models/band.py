from flask_app.config.mysqlconnection import connectToMySQL
from flask_app import app
from flask import render_template, redirect, request, session, flash
from flask_bcrypt import Bcrypt


class Band:
    def __init__(self, data):
        self.id = data['id']
        self.founder_id = data['founder_id']
        self.band_name = data['band_name']
        self.genre = data['genre']
        self.home_city = data['home_city']
        self.founding_member = data['founding_member']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']


    @classmethod
    def get_all_bands(cls):
        query = "SELECT bands.id, bands.founder_id, bands.band_name, bands.genre, bands.home_city, bands.created_at, bands.updated_at, GROUP_CONCAT(users.first_name, ' ', users.last_name) AS founding_member FROM bands JOIN users ON bands.founder_id = users.id GROUP BY id;"
        results = connectToMySQL('band_together').query_db(query)
        print('````````````````````````')
        print(results)
        # Create an empty list to append our instances of bands
        bands = []
        # Iterate over the db results and create instances of bands with cls.
        for band in results:
            print(results)
            bands.append(cls(band))
        return bands

    @classmethod
    def save_band(cls, data):
        query = "INSERT INTO bands (founder_id, band_name, genre, home_city) VALUES (%(founder_id)s, %(band_name)s, %(genre)s, %(home_city)s);"
        return connectToMySQL('band_together').query_db(query, data)

    @staticmethod
    def validate_new_band(form_data):
        is_valid = True

        # Band Name
        # Submission required - make sure it's not an empty string
        if len(form_data['band_name']) == 0:
            flash("Band Name is required.", "band_name")
            is_valid = False
        # is at least 2 characters
        elif len(form_data['band_name']) < 2:
            flash("Band Name must be at least 2 characters in length.", "band_name")
            is_valid = False

        # Genre
        # Submission required - make sure it's not an empty string
        if len(form_data['genre']) == 0:
            flash("Genre is required.", "genre")
            is_valid = False
        # is at least 10 characters
        elif len(form_data['genre']) < 2:
            flash("Genre must be at least 2 characters in length.", "genre")
            is_valid = False

        # Home City
        # Submission required - make sure it's not an empty string
        if len(form_data['home_city']) == 0:
            flash("Home City is required.", "home_city")
            is_valid = False
        # is at least 10 characters
        elif len(form_data['home_city']) < 2:
            flash("Home City must be greater than 2 characters in length.", "home_city")
            is_valid = False

        return is_valid
