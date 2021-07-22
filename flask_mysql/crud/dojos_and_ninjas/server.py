# python3 -m pipenv install flask pymysql
# python3 -m pipenv shell
# python3 server.py

from flask_app.controllers import ninjas, dojos

from flask_app import app


if __name__ == '__main__':   # Ensure this file is being run directly and not from a different module
    app.run(debug=True)    # Run the app in debug mode.
