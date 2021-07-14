# python3 -m pipenv install flask jinja2 - Make pipfile and pipfile.lock
# python3 -m pipenv shell - Enter into shell
# python3 server.py - Start your server
# Import Flask to allow us to create our app
from flask import Flask, render_template
app = Flask(__name__)

# Create a route in which the data is declared and then sent to the template engine to be rendered


@app.route('/')
def user_data():
    # Return the result of the render_template method, passing in the name of our HTML file
    users = [
        {'first_name': 'Michael', 'last_name': 'Choi'},
        {'first_name': 'John', 'last_name': 'Supsupin'},
        {'first_name': 'Mark', 'last_name': 'Guillen'},
        {'first_name': 'KB', 'last_name': 'Tonel'}
    ]

    return render_template('index.html', users=users)


if __name__ == '__main__':   # Ensure this file is being run directly and not from a different module
    app.run(debug=True)    # Run the app in debug mode.
