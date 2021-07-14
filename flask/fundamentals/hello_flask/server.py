# Import Flask to allow us to create our app
from flask import Flask, render_template
# Create a new instance of the Flask class called 'app'
app = Flask(__name__)


# The '@' decorator associates this route with the function immediately following
@app.route('/')
def hello_world():
    return 'Hello World!'  # Return the string 'Hello World!' as a response


@app.route('/lists')
def render_lists():
    # Soon enough, we'll get data from a database, but for now, we're hard coding data
    student_info = [
        {'name': 'Michael', 'age': 35},
        {'name': 'John', 'age': 30},
        {'name': 'Mark', 'age': 25},
        {'name': 'KB', 'age': 27}
    ]
    return render_template("lists.html", random_numbers=[3, 1, 5], students=student_info)


@app.route('/success')
def success():
    return 'Success!'


# for a route '/hello/____' anything after '/hello/' gets passed as a variable 'name'
@app.route('/hello/<luna>')
def hello(luna):
    print(luna)
    return "Hello, " + luna


# for a route '/users/____/____', two parameters in the url get passed as username and id
@app.route('/users/<username>/<id>')
def show_user_profile(username, id):
    print(username)
    print(id)
    return "username: " + username + ", id: " + id


# @app.route('/foo')          Any other routes
# def that_routes_foo():
    # return 'Happy Coding!'  Return the string 'Happy Coding!' as a response
if __name__ == '__main__':   # Ensure this file is being run directly and not from a different module
    app.run(debug=True)    # Run the app in debug mode.
