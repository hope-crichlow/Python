from flask import Flask  # Import Flask to allow us to create our app

# Create a new instance of the Flask class called 'app'
app = Flask(__name__)

# Create a root route("/") that responds with "Hello World!"


@app.route("/")
def hello_world():
    return "Hello World!"  # Return the string 'Hello World!' as a response

# Create a route that responds with "Dojo!"


@app.route("/dojo")
def that_routes_dojo():
    return "Dojo!"  # Return the string 'Dojo!' as a response

# Create a route that responds with "Hi" and whatever name is in the URL after / say/


@app.route("/say/<hope>")
def say(hope):
    print(hope)
    return "Hi, " + hope  # Return the string 'Hi, hope' as a response

# Create a route that responds with the given word repeated as many times as specified in the URL


@app.route("/<number>/<word>")
def multiply(number, word):
    # NINJA BONUS: Ensure the names provided in the 3rd task are strings
    message = str(str(word) * int(number))
    print(message)
    return message  # Return a string of {number} {words} as a response


# Ensure this file is being run directly and not from a different module
if (__name__ == "__main__"):
    app.run(debug=True)  # Run the app in debug mode.
