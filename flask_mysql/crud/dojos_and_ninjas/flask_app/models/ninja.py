
# import the function that will return an instance of a connection
from flask_app.config.mysqlconnection import connectToMySQL
from flask_app.models.dojo import Dojo
# # model the class after the Ninjas table from our database


class Ninja:
    def __init__(self, data):
        self.ninja_id = data['ninja_id']
        self.dojo_id = data['dojo_id']
        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.age = data['age']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
    # Now we use class methods to query our database

    @classmethod
    def get_all_ninjas_from_dojo(cls, dojo_id):
        query = "SELECT * FROM ninjas WHERE dojo_id=%(dojo_id)s;"
        # make sure to call the connectToMySQL function with the schema you are targeting.
        data = {
            "dojo_id": dojo_id
        }
        results = connectToMySQL('dojos_and_ninjas').query_db(query, data)
        # Create an empty list to append our instances of ninjas
        ninjas = []
        # Iterate over the db results and create instances of ninjas with cls.
        for ninja in results:
            ninjas.append(cls(ninja))
        return ninjas
    #     # This is just an example of what you could do with the results.
    #     if len(results) > 0:
    #         return results[0]
    #     else:
    #         return False

    @classmethod
    def save_ninja(cls, data):
        query = "INSERT INTO ninjas (dojo_id, first_name, last_name, age) VALUES (%(dojo_id)s, %(first_name)s, %(last_name)s, %(age)s);"

        # data is a dictionary that's being passed into the save method from server.py
        return connectToMySQL('dojos_and_ninjas').query_db(query, data)
