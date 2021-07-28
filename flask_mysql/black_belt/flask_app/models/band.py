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
