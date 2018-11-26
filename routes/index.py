from flask import render_template
from . import routes

#FLASK_ENV=development FLASK_APP=python-projects flask run

@routes.route('/')
def index():
    return render_template('index.html')