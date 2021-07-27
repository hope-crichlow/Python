from flask_app import app
import os, petpy


from flask_app.controllers import pets
# from flask_app.models import Pet, Petfinder

if __name__ == "__main__":
    app.run(debug=True)
