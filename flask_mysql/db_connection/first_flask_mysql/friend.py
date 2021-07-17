# import the function that will return an instance of a connection
from mysqlconnection import connectToMySQL
# model the class after the friend table from our database


class Friend:
    def __init__(self, data):
        self.id = data['friend_id']
        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.occupation = data['occupation']
        self.updated_at = data['updated_at']
        self.created_at = data['created_at']
    # Now we use class methods to query our database

    @classmethod
    def get_all(cls):
        query = "SELECT * FROM friends;"
        # make sure to call the connectToMySQL function with the schema you are targeting.
        results = connectToMySQL('first_flask').query_db(query)
        # Create an empty list to append our instances of friends
        friends = []
        # Iterate over the db results and create instances of friends with cls.
        for friend in results:
            friends.append(cls(friend))
        return friends

    @classmethod
    def get_one(cls, friend_id):
        query = "SELECT * FROM friends WHERE id=%(friend_id)d;"

        data = {
            "friend_id": friend_id
        }
        results = connectToMySQL('first_flask').query_db(query, data)
        # This is just an example of what you could do with the results.
        if len(results) > 0:
            return results[0]
        else:
            return False

    @classmethod
    def save(cls, data):
        query = "INSERT INTO friends (first_name, last_name, occupation, created_at, updated_at) VALUES (%(first_name)s, %(last_name)s, %(occupation)s, NOW(), NOW());"

        # data is a dictionary that's being passed into the save method from server.py
        return connectToMySQL('first_flask').query_db(query, data)
