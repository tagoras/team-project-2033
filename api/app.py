from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager, login_user, current_user
from flask_cors import CORS
import json
from werkzeug.security import generate_password_hash, check_password_hash
import re

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data/api.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)
CORS(app)


def empty_values(dictionary):
    for key in dictionary:
        if dictionary[key] == '':
            return 'Empty'
    return 0


@app.route('/hello_world')
def hello_world() -> json:
    # just for testing : return a hello world json object, for debugging api calls
    return {'title': "Hello!",
            'content': "Hello World"}


@app.route('/register', methods=['GET', 'POST'])
def register() -> json:
    # POST a data to database and GET a returned statuscode message
    if request.is_json:
        registration_form = request.json
        # Any empty values
        if empty_values(registration_form) == -1:
            return {
                'status': -1,
                'message': "Registration failed: Fill all fields"
            }

        # Password Validating
        password_size = len(registration_form['password'])
        password_checker = re.compile(r'(?=.*\d)(?=.*[a-z])(?=.*[A-Z])(?=.*[*?!^+%&()=}{$#@<>])')
        if password_checker.match(registration_form['password']):
            return {
                'status': -1,
                'message': "Registration failed: Please check password"
            }
        elif 6 > password_size > 12:
            return {
                'status': -1,
                'message': "Registration failed: Please check password"
            }

        # Email Validating
        regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
        if not re.search(regex, registration_form['email']):
            return {
                'status': -1,
                'message': "Registration failed: Please check your email"
            }

        # Postcode Validation
        regex = r'[A-Z]{1,2}[0-9R][0-9A-Z]? [0-9][A-Z]{2}'
        if not re.search(regex, registration_form['postcode']):
            return {
                'status': -1,
                'message': "Registration failed: Please check postcode"
            }

        # One way encrypt
        registration_form['password'] = generate_password_hash(registration_form['password'])
        registration_form['postcode'] = generate_password_hash(registration_form['postcode'])

        # This is really weird, connection is established but breaks for no reason
        # TODO: Investigate
        try:
            user = User.query.filter_by(email=registration_form['email']).first()
            if user:
                return {
                    'status': -1,
                    'message': "Registration failed: Email is already taken!"
                }
        except Exception as e:
            print(e)
            return {
                'status': -1,
                'message': "Registration failed: Email might already be taken, try again later"
            }
        try:
            new_user = User(username=registration_form['username'],
                            email=registration_form['email'],
                            postcode=registration_form['postcode'],
                            password=registration_form['password'])
            db.session.add(new_user)
            db.session.commit()
            return {
                'status': 0,
                'message': "Account successfully registered"
            }
        except Exception as e:
            print(e)
            return {
                'status': -1,
                'message': "Registration failed: Internal error"
            }
    else:
        return {
            'status': -1,
            'message': "Registration failed: This is no json!!"
        }


@app.route('/login', methods=['GET', 'POST'])
def login() -> json:
    if request.is_json:
        login_form = request.json

        if empty_values(login_form) == -1:
            return {
                'status': -1,
                'message': "Login failed: Fill all fields"
            }

        user = User.query.filter_by(username=login_form['username']).first()

        if not user or not check_password_hash(user.password, login_form['password']):
            return {
                'status': -1,
                'message': "Login failed: Username or password is incorrect!"
            }
        try:
            login_user(user)
            return {
                'status': 0,
                'message': "User successfully logged in"
            }
        except Exception as e:
            print(e)
            return {
                'status': -1,
                'message': "Login failed: Username or password might be incorrect. Please try again later"
            }
    else:
        return {
            'status': -1,
            'message': "Login failed: This is no json!!"
        }


if __name__ == "__main__":

    my_host = "localhost"
    my_port = 5000

    login_manager = LoginManager()
    login_manager.login_view = 'users.login'
    login_manager.init_app(app)

    from models import User


    @login_manager.user_loader
    def load_user(username) -> User:
        try:
            return User.query.get(username)
        except Exception as e:
            print("load_user failed\n")
            print(e)
            return -1


    app.run(host=my_host, port=my_port, debug=True)
