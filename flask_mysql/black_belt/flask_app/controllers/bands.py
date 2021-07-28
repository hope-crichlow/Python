from flask_app import app
from flask import render_template, redirect, request, session, flash
from flask_bcrypt import Bcrypt
from flask_app.models.band import Band
from flask_app.models.user import User

bcrypt = Bcrypt(app)


# @app.route('/')
# def index():
#     return render_template('index.html')


# @app.route('/new')
# def new_band():
#     if 'user_id' not in session:
#         return redirect('/')

#     return render_template('new_band.html')


# @app.route('/create', methods=['POST'])
# def create_band():
#     band_validation = Band.validate_new_band(request.form)
#     if band_validation == False:
#         return redirect('/bands/new')
#     else:
#         data = {
#             "founder_id": session['user_id'],
#             "band_name": request.form['band_name'],
#             "genre": request.form['genre'],
#             "home_city": request.form['home_city'],
#             "founding_member": request.form['founding_member']
            
#         }

#     print('****************')
#     print(data)
#     Band.save_band(data)

#     # NEVER RENDER ON A POST
#     return redirect('/dashboard')


