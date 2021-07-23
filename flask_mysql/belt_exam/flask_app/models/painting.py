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
        query = "SELECT * FROM paintings JOIN users ON users.id = paintings.user_id;"
        #SELECT painting.title, user.first_name, user.last_name FROM paintings JOIN users ON paintings.user_id = users.id
        #"SELECT * FROM paintings JOIN users ON users.id = paintings.user_id;"
        # make sure to call the connectToMySQL function with the schema you are targeting.
        results = connectToMySQL('belt_exam').query_db(query)
        print('````````````````````````')
        print(results , "\n")
        # Create an empty list to append our instances of paintings
        paintings = []
        # Iterate over the db results and create instances of paintings with cls.
        for painting in results:
            paintings.append(cls(painting))
        return paintings
        # if len(results) > 0:
        #     return cls(results[0])
        # else:
        #     return False

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
        query = "UPDATE paintings SET title=%(title)s, description=%(description)s, price=%(price)s WHERE id=%(id)s;"
        #, quantity=%(quantity)s, artist=%(artist)s, num_purchased=%(num_purchased)s
        print("lalalalalalalalalal*****************")
        print(data)

        results = connectToMySQL('belt_exam').query_db(query, data)
        print(results)

        return results
