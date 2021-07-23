from flask_app.config.mysqlconnection import connectToMySQL
from flask_app import app
from flask import render_template, redirect, request, session, flash
from flask_bcrypt import Bcrypt



class Recipe:
    def __init__(self, data):
        self.id = data['id']
        self.user_id = data['user_id']
        self.name = data['name']
        self.description = data['description']
        self.instructions = data['instructions']
        self.under_thirty = data['under_thirty']
        self.date_made = data['date_made'].strftime("%B, %d, %Y")
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
    # Now we use class methods to query our database

    @classmethod
    def get_all(cls):
        query = "SELECT * FROM recipes;"
        # make sure to call the connectToMySQL function with the schema you are targeting.
        results = connectToMySQL('recipes').query_db(query)
        print('````````````````````````')
        print(results)
        # Create an empty list to append our instances of recipes
        recipes = []
        # Iterate over the db results and create instances of recipes with cls.
        for recipe in results:
            recipes.append(cls(recipe))
        return recipes
        # if len(results) > 0:
        #     return cls(results[0])
        # else:
        #     return False

    @classmethod
    def get_one(cls, id):
        query = "SELECT * FROM recipes WHERE id=%(id)s;"

        data = {
            "id": id
        }
        results = connectToMySQL('recipes').query_db(query, data)
        print('/////////', results)
        recipe = cls(results[0])
        return recipe
