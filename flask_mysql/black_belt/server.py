# python3 -m pipenv install flask flask-bcrypt pymysql requests python-dotenv
# python3 -m pipenv shell
# python3 server.py
from flask_app import app
from flask_app.controllers import users
if __name__ == '__main__':
    app.run(debug=True)
