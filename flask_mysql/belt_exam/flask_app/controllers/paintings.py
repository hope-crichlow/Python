# python3 -m pipenv install flask flask-bcrypt pymysql
# python3 -m pipenv shell
# python3 server.py
from flask_app import app
from flask import render_template, redirect, request, session, flash
from flask_bcrypt import Bcrypt
from flask_app.models.user import User
from flask_app.models.painting import Painting





# @app.route('/recipes/<int:id>')
# def view_recipe(id):
#     get_selected = Recipe.get_one(id)
#     return render_template('view.html', selected_recipe=get_selected)
