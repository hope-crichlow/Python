from flask_app.config.mysqlconnection import connectToMySQL
from flask_app import app
from flask import render_template, redirect, request, session, flash
from flask_bcrypt import Bcrypt



class Painting:
    def __init__(self, data):
        self.id = data['id']
        self.user_id = data['user_id']
        self.title = data['title']
        self.description = data['description']
        self.price = data['price']
        self.artist = data['artist']
        self.quantity = data['quantity']
        self.num_purchased = data['num_purchased']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
    # Now we use class methods to query our database

    @classmethod
    def get_all_paintings(cls):
        query ="SELECT paintings.id, paintings.title, paintings.user_id, paintings.description, paintings.price, paintings.quantity, paintings.num_purchased, paintings.created_at, paintings.updated_at, GROUP_CONCAT(users.first_name, ' ', users.last_name) AS artist FROM paintings JOIN users ON paintings.user_id = users.id GROUP BY id;"

        results = connectToMySQL('belt_exam').query_db(query)
        print('````````````````````````')
        print(results)
        # Create an empty list to append our instances of paintings
        paintings = []
        # Iterate over the db results and create instances of paintings with cls.
        for painting in results:
            print(results)
            paintings.append(cls(painting))
        return paintings

    @classmethod
    def get_one(cls, id):
        query = "SELECT * FROM paintings WHERE id=%(id)s;"

        data = {
            "id": id
        }
        results = connectToMySQL('belt_exam').query_db(query, data)
        print('/////////', results)
        painting = cls(results[0])
        return painting

    @classmethod
    def edit_one(cls, data):
        query = "UPDATE paintings SET title=%(title)s, description=%(description)s, price=%(price)s WHERE id=%(id)d;"
    
        print("lalalalalalalalalal*****************")
        print(data)

        results = connectToMySQL('belt_exam').query_db(query, data)
        print(results)

        return results

    @classmethod
    def save_painting(cls, data):
        query = "INSERT INTO paintings (user_id, title, description, price) VALUES (%(user_id)s, %(title)s, %(description)s, %(price)s);"
        return connectToMySQL('belt_exam').query_db(query, data)

    @staticmethod
    def validate_new_painting(form_data):
        is_valid = True

        # Title
        # Submission required - make sure it's not an empty string
        if len(form_data['title']) == 0:
            flash("Title is required.", "title")
            is_valid = False
        # is at least 2 characters
        elif len(form_data['title']) < 2:
            flash("Title must be at least 2 characters in length.", "title")
            is_valid = False
        
        # Description
        # Submission required - make sure it's not an empty string
        if len(form_data['description']) == 0:
            flash("Description is required.", "description")
            is_valid = False
        # is at least 10 characters
        elif len(form_data['description']) < 10:
            flash("Description must be at least 10 characters in length.", "description")
            is_valid = False

        # Price
        # Submission required - make sure it's not an empty string
        if len(form_data['price']) == 0:
            flash("Price is required.", "price")
            is_valid = False
        # is at least 10 characters
        elif len(form_data['price']) < 1:
            flash("Price must be greater than $10.", "price")
            is_valid = False

        return is_valid

    @classmethod
    def delete_one(cls, data):
        query = "DELETE FROM paintings WHERE id=%(id)s;"
        return connectToMySQL('belt_exam').query_db(query, data)