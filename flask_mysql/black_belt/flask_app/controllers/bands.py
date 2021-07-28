from flask_app import app
from flask import render_template, redirect, request, session, flash
from flask_bcrypt import Bcrypt
from flask_app.models.user import User
from flask_app.models.band import Band




# @app.route('/create', methods=['POST'])
# def create_painting():
#     painting_validation = Painting.validate_new_painting(request.form)
#     if painting_validation == False:
#         return redirect('/paintings/new')
#     else:
#         data = {
#             "user_id": session['user_id'],
#             "title": request.form['title'],
#             "description": request.form['description'],
#             'price': request.form['price']
#         }

#     print('****************')
#     print(data)
#     Painting.save_painting(data)

#     # NEVER RENDER ON A POST
#     return redirect('/dashboard')
