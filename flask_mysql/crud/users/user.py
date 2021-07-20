# import the function that will return an instance of a connection
from mysqlconnection import connectToMySQL
from datetime import datetime
# model the class after the user table from our database


class User:
    def __init__(self, data):
        self.user_id = data['user_id']
        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.email = data['email']
        self.created_at = data['created_at'].strftime("%B, %d, %Y")
        self.updated_at = data['updated_at'].strftime("%B, %d, %Y at %I:%M:%p")
        self.created_at_date = self.created_at
    # Now we use class methods to query our database

    @classmethod
    def get_all(cls):
        query = "SELECT * FROM users;"
        # make sure to call the connectToMySQL function with the schema you are targeting.
        results = connectToMySQL('users').query_db(query)
        # Create an empty list to append our instances of users
        users = []
        # Iterate over the db results and create instances of users with cls.
        for user in results:
            users.append(cls(user))
        return users

    @classmethod
    def get_one(cls, user_id):
        # user_id = int(user_id)
        query = "SELECT * FROM users WHERE user_id=%(user_id)s;"

        data = {
            "user_id": user_id
        }
        print(data)

        results = connectToMySQL('users').query_db(query, data)
        print(results)

        # This is just an example of what you could do with the results.
        # Because results returns a LIST OF DICTIONARIES:
        if len(results) > 0:
            return cls(results[0])
        else:
            return False

    @classmethod
    def save(cls, data):
        query = "INSERT INTO users (first_name, last_name, email, created_at, updated_at) VALUES (%(first_name)s, %(last_name)s, %(email)s, NOW(), NOW());"

        # data is a dictionary that's being passed into the save method from server.py
        return connectToMySQL('users').query_db(query, data)

    @classmethod
    def edit_one(cls, data):
        query = "UPDATE users SET first_name=%(first_name)s, last_name=%(last_name)s, email=%(email)s, updated_at=NOW() WHERE user_id=%(user_id)s;"

        print(data)

        results = connectToMySQL('users').query_db(query, data)
        print(results)

        # This is just an example of what you could do with the results.
        # Because results returns a LIST OF DICTIONARIES:
        # if len(results) > 0:
        #     return cls(results[0])
        # else:
        #     return False
        return results
