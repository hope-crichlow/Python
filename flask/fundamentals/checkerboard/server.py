# Import Flask to allow us to create our app
from flask import Flask, render_template
# Create a new instance of the Flask class called 'app'
app = Flask(__name__)


# http://localhost:5000 - Display 8 by 8 checkerboard
@app.route('/')
def checkered_pair():
    return render_template('index.html', row_pair=4, column_pair=4,  first_color="red", second_color="black")


# http://localhost:5000/4 - Display 8 by 4 checkerboard
@app.route('/<x>')
def checkered_rows(x):
    x = int(int(x) / 2)
    print(x)
    return render_template('index.html', row_pair=x, column_pair=4,  first_color="red", second_color="black")


# http: // localhost: 5000/(x)/(y) - should display x by y checkerboard.
@app.route('/<x>/<y>')
def checkered_board(x, y):  # find a solution using if [i] % 2 yaddah yahh
    x = int(int(x) / 2)
    y = int(int(y) / 2)
    print(x, y)
    return render_template('index.html', row_pair=x, column_pair=y, first_color="red", second_color="black")


if __name__ == '__main__':   # Ensure this file is being run directly and not from a different module
    app.run(debug=True)    # Run the app in debug mode.
