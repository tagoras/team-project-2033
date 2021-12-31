from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
import json
from werkzeug.security import generate_password_hash, check_password_hash
import re
from flask_jwt_extended import create_access_token, get_jwt_identity, jwt_required, JWTManager

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data/api.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = 'This is supposed to be a secret key, thank you for your understanding.'
db = SQLAlchemy(app)
CORS(app)

app.config["JWT_SECRET_KEY"] = "Yet again another super secret key, thank you for your understanding."
jwt = JWTManager(app)


def empty_values(dictionary):
    for key in dictionary:
        if dictionary[key] == '':
            return 'Empty'
    return 0


def requires_roles(current_user, roles):
    if current_user.role not in roles:
        return jsonify({
            'status': 403,
            'message': "User doesn't have permission to this page"
        })


@app.route('/hello_world')
def hello_world() -> json:
    # just for testing : return a hello world json object, for debugging api calls
    return jsonify({'title': "Hello!",
                    'content': "Hello World"},
                   request.json), 200


@app.route('/hello_world/jwt')
@jwt_required()
def hello_world_jwt() -> json:
    current_user = get_jwt_identity()
    # just for testing : return a hello world json object, for debugging api calls
    return jsonify({'title': "Hello!",
                    'content': "Hello World, I am logged in, amazing!"},
                   request.json, current_user), 200


@app.route('/register', methods=['GET', 'POST'])
def register() -> json:
    # POST a data to database and GET a returned statuscode message
    if request.is_json and ("username" and "password" and "email" and "postcode" in request.json):
        registration_form = request.json
        # Any empty values
        if empty_values(registration_form) == -1:
            return jsonify({
                'status': -1,
                'message': "Registration failed: Fill all fields"
            }), 406

        # Password Validating
        password_size = len(registration_form['password'])
        password_checker = re.compile(r'(?=.*\d)(?=.*[a-z])(?=.*[A-Z])(?=.*[*?!^+%&()=}{$#@<>])')
        if password_checker.match(registration_form['password']):
            return jsonify({
                'status': -1,
                'message': "Registration failed: Please check password"
            }), 406
        elif 6 > password_size > 12:
            return jsonify({
                'status': -1,
                'message': "Registration failed: Please check password"
            }), 406

        # Email Validating
        regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
        if not re.search(regex, registration_form['email']):
            return jsonify({
                'status': -1,
                'message': "Registration failed: Please check your email"
            }), 406

        # Postcode Validation
        regex = r'[A-Z]{1,2}[0-9R][0-9A-Z]? [0-9][A-Z]{2}'
        if not re.search(regex, registration_form['postcode']):
            return jsonify({
                'status': -1,
                'message': "Registration failed: Please check postcode"
            }), 406

        # One way encrypt
        registration_form['password'] = generate_password_hash(registration_form['password'])
        registration_form['postcode'] = generate_password_hash(registration_form['postcode'])

        try:
            user = User.query.filter_by(email=registration_form['email']).first()
            if user:
                return jsonify({
                    'status': -1,
                    'message': "Registration failed: Email is already taken!"
                }), 406
        except Exception as e:
            print(e)
            return jsonify({
                'status': -1,
                'message': "Registration failed: Email might already be taken, try again later"
            }), 500

        try:
            user = User.query.filter_by(username=registration_form['username']).first()
            if user:
                return jsonify({
                    'status': -1,
                    'message': "Registration failed: Username is already taken!"
                }), 406
        except Exception as e:
            print(e)
            return jsonify({
                'status': -1,
                'message': "Registration failed: Username might already be taken, try again later"
            }), 500

        try:
            new_user = User(username=registration_form['username'],
                            email=registration_form['email'],
                            postcode=registration_form['postcode'],
                            password=registration_form['password'],
                            role='user')
            db.session.add(new_user)
            db.session.commit()
            return jsonify({
                'status': 0,
                'message': "Account successfully registered"
            }), 201
        except Exception as e:
            print(e)
            return jsonify({
                'status': -1,
                'message': "Registration failed: Internal error"
            }), 500
    else:
        return jsonify({
            'status': -1,
            'message': "Registration failed: This is no json!!"
        }), 406


@app.route('/login', methods=['GET', 'POST'])
def login() -> json:
    if request.is_json and ("username" and "password" in request.json):
        login_form = request.json

        if empty_values(login_form) == -1:
            return jsonify({
                'status': -1,
                'message': "Login failed: Fill all fields"
            }), 406

        user = User.query.filter_by(username=login_form['username']).first()

        if not user or not check_password_hash(user.password, login_form['password']):
            return jsonify({
                'status': -1,
                'message': "Login failed: Username or password is incorrect!"
            }), 406
        try:
            access_token = create_access_token(identity=user)
            return jsonify({
                'status': 0,
                'message': "User successfully logged in"},
                access_token=access_token), 202
        except Exception as e:
            print(e)
            return jsonify({
                'status': -1,
                'message': "Login failed: Username or password might be incorrect. Please try again later"
            }), 500
    else:
        return jsonify({
            'status': -1,
            'message': "Login failed: This is no json!!"
        }), 406


@app.route("/logout")
@jwt_required()
def logout() -> json:
    try:
        # This should be handled in the front-end !!!
        # This is just a placeholder

        return {
                   'status': 0,
                   'message': "Logout successful."
               }, 200
    except Exception as e:
        print(e)
        return {
                   'status': -1,
                   'message': "Logout failed: check console."
               }, 500


@app.route("/admin")
@jwt_required()
def admin() -> json:
    current_user = get_jwt_identity()
    requires_roles(current_user, 'admin')
    return jsonify({
        'status': 200,
        'message': "Work in progress"
    })


if __name__ == "__main__":
    my_host = "localhost"
    my_port = 5000

    from models import User

    app.run(host=my_host, port=my_port, debug=True)
