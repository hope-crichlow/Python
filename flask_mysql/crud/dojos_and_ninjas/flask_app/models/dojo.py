# # import the function that will return an instance of a connection
from flask_app.config.mysqlconnection import connectToMySQL
# from flask_app.models.ninja import Ninja
# model the class after the Dojos table from our database


class Dojo:
    def __init__(self, data):
        self.dojo_id = data['dojo_id']
        self.name = data['name']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
    # Now we use class methods to query our database

    @classmethod
    def get_all(cls):
        query = "SELECT * FROM dojos;"
        # make sure to call the connectToMySQL function with the schema you are targeting.
        results = connectToMySQL('dojos_and_ninjas').query_db(query)
        # Create an empty list to append our instances of dojos
        dojos = []
        # Iterate over the db results and create instances of dojos with cls.
        for dojo in results:
            dojos.append(cls(dojo))
        return dojos

    @classmethod
    def get_one(cls, dojo_id):
        query = "SELECT * FROM dojos WHERE dojo_id=%(dojo_id)s;"

        data = {
            "dojo_id": dojo_id
        }
        results = connectToMySQL('dojos_and_ninjas').query_db(query, data)
        dojo = cls(results[0])
        return dojo
    #     print(results)
    #    # Get the singular dojo from the list of dictionaries
    #     if len(results) > 0:
    #         return cls(results[0])
    #     else:
    #         return False
    

    @classmethod
    def save_dojo(cls, data):
        query = "INSERT INTO dojos (name) VALUES (%(name)s);"

        # data is a dictionary that's being passed into the save method from server.py
        return connectToMySQL('dojos_and_ninjas').query_db(query, data)
