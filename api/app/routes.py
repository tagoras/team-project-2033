from api.app import app
from flask import request, Blueprint
from api.app import logging_system
import json

routes = Blueprint('routes', __name__)


@app.route('/')
def index():
    return 'Index Page'


@app.route('/hello_world')
def hello_world() -> json:
    # just for testing : return a hello world json object, for debugging api calls
    return {'title': "Hello!",
            'content': "Hello World"}


@app.route('/register2', methods=['GET', 'POST'])
def register():

    # Retrieve data from Front-End
    registration_form = request.get_data()

    # Output data to Front-End
    return logging_system.registration(registration_form)


@app.route('/login', methods=['GET', 'POST'])
def login():

    # Retrieve data from Front-End
    login_form = request.get_data()

    # Output data to Front-End
    return logging_system.login(login_form)
