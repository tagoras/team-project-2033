import json
import re
from flask_login import login_user
from werkzeug.security import generate_password_hash
from werkzeug.security import check_password_hash
from app.models import User
from app import db


def empty_values(dictionary):
    for key in dictionary:
        if dictionary[key] == '':
            return -1
    return 0


def registration(reg_info):
    # Converts JSON object into dictionary
    reg_dictionary = json.loads(reg_info)

    # Any empty values
    if empty_values(reg_dictionary) == -1:
        return {
            'status': -1,
            'message': "Registration failed: Fill all fields"
        }

    # Username Exists?
    username_size = len(reg_dictionary['username'])
    username_checker = User.query.filter_by(username=reg_dictionary['username']).first()
    if not(6 < username_size < 15):
        return {
            'status': -1,
            'message': "Registration failed: Username is too big/small"
        }
    elif username_checker:
        return {
            'status': -1,
            'message': "Registration failed: Username exists already"
        }

    # Password Validating
    password_size = len(reg_dictionary['password'])
    password_checker = re.compile(r'(?=.*[a-zA-Z\d*?!^+%&()=}{$#@<>])')
    if not (password_checker.match(reg_dictionary['password'])):
        return {
            'status': -1,
            'message': "Registration failed: Please check password"
        }
    elif not (6 < password_size < 12):
        return {
            'status': -1,
            'message': "Registration failed: Please check password"
        }

    # Email Validating
    regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
    if not re.search(regex, reg_dictionary['email']):
        return {
            'status': -1,
            'message': "Registration failed: Please check your email"
        }

    # Postcode Validation
    regex = r'[A-Z]{1,2}[0-9R][0-9A-Z]? [0-9][A-Z]{2}'
    if not re.search(regex, reg_dictionary['postcode']):
        return {
            'status': -1,
            'message': "Registration failed: Please check postcode"
        }

    # One way encrypt
    reg_dictionary["password"] = generate_password_hash(reg_dictionary["password"])
    reg_dictionary["postcode"] = generate_password_hash(reg_dictionary["postcode"])
    print(len(reg_dictionary['password']))

    try:
        new_user = User(username=reg_dictionary['username'],
                        email=reg_dictionary['email'],
                        postcode=reg_dictionary['postcode'],
                        password=reg_dictionary['password'])
        db.session.add(new_user)
        db.session.commit()
        return {
            'status': 200,
            'message': "Account successfully registered"
        }
    except Exception as e:
        print(e)
        return {
            'status': -1,
            'message': "Registration failed: Internal error"
        }


def login(login_info):
    # Converts JSON object into dictionary
    login_dictionary = json.loads(login_info)

    # Any empty values
    if empty_values(login_dictionary) == -1:
        return {
            'status': -1,
            'message': "Login failed: Fill all fields"
        }

    user = User.query.filter_by(username=login_dictionary['username']).first()

    if not user or not check_password_hash(user.password, login_dictionary['password']):
        return {
            'status': -1,
            'message': "Login failed: Username or password is incorrect!"
        }
    try:
        login_user(user)
        return {
            'status': 200,
            'message': "User successfully logged in"
        }
    except Exception as e:
        print(e)
        return {
            'status': -1,
            'message': "Login failed: Username or password might be incorrect. Please try again later"
        }
