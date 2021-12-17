from app import app
from flask import request
import logging_system
import json


@app.route('/hello_world')
def hello_world() -> json:
    # just for testing : return a hello world json object, for debugging api calls
    return {'title': "Hello!",
            'content': "Hello World"}


@app.route('/register2', methods=['GET', 'POST'])
def register():

    # Retrieve data from Front-End
    registration_form = request.get_data()
    return logging_system.registration(registration_form)
