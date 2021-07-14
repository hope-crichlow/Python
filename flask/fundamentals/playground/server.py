# Import Flask to allow us to create our app
from flask import Flask, render_template
# Create a new instance of the Flask class called 'app'
app = Flask(__name__)


@app.route("/")
def hello_world():
    return "Hello World!"


@app.route('/play')  # Have the /play route render a template with 3 blue boxes
def play():
    return render_template('index.html', boxes=3, color="rgb(159, 197, 248, 1)")


# Have the /play/<x> route render a template with x number of blue boxes
@app.route('/play/<x>')
def play_more(x):
    return render_template('index.html', boxes=int(x), color="rgb(159, 197, 248, 1)")


# Have the /play/<x>/<color> route render a template with x number of boxes the color of the provided value
@app.route('/play/<x>/<color>')
def play_more_color(x, color):
    return render_template('index.html', boxes=int(x), color=color)


if __name__ == '__main__':   # Ensure this file is being run directly and not from a different module
    app.run(debug=True)    # Run the app in debug mode.
