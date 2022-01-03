# IMPORTS
import datetime
import json
import re

import flask
from flask import Flask, request, jsonify
from flask_cors import CORS
from flask_jwt_extended import create_access_token, get_jwt_identity, jwt_required, JWTManager
from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash, check_password_hash

# CONFIG
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data/api.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = 'This is supposed to be a secret key, thank you for your understanding.'
db = SQLAlchemy(app)
CORS(app)

app.config["JWT_SECRET_KEY"] = "Yet again another super secret key, thank you for your understanding."
jwt = JWTManager(app)


# Searches through a dictionary to see if any key has an empty value
def empty_values(dictionary):
    for key in dictionary:
        if dictionary[key] == '':
            return 'Empty'
    return 0


# just for testing : return a hello world json object, for debugging api calls
@app.route('/hello_world')
def hello_world() -> json:
    return jsonify({'title': "Hello!",
                    'content': "Hello World"},
                   request.json), 200


# just for testing : return a hello world json object, for debugging api calls
@app.route('/hello_world/jwt')
@jwt_required()
def hello_world_jwt() -> json:
    current_user = get_jwt_identity()
    return jsonify({'title': "Hello!",
                    'content': "Hello World, I am logged in, amazing!"},
                   request.json, current_user), 200


# Registers the user if they don't have an account
@app.route('/register', methods=['GET', 'POST'])
def register() -> json:
    # Grabs info from front-end and checks if it json
    if request.is_json and ("username" and "password" and "email" and "postcode" in request.json):
        # Converts json object into dictionary and checks if there are empty
        registration_form = request.json
        if empty_values(registration_form) == -1:
            return jsonify({
                'status': -1,
                'message': "Registration failed: Fill all fields"
            }), 406

        # Password Validating, 1 Uppercase, 1 Lowercase, 1 Digit and 1 Special Character, length between 6 and 12
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

        # Email Validating, Looks similar to an email
        regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
        if not re.search(regex, registration_form['email']):
            return jsonify({
                'status': -1,
                'message': "Registration failed: Please check your email"
            }), 406

        # Postcode Validation, Format: AA1 2BB
        regex = r'[A-Z]{1,2}[0-9R][0-9A-Z]? [0-9][A-Z]{2}'
        if not re.search(regex, registration_form['postcode']):
            return jsonify({
                'status': -1,
                'message': "Registration failed: Please check postcode"
            }), 406

        # One way encrypt
        registration_form['password'] = generate_password_hash(registration_form['password'])
        registration_form['postcode'] = generate_password_hash(registration_form['postcode'])

        # An attempt to check if the email given has been already used for registering
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

        # An attempt to check if the username given has been already used for registering
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

        # An attempt to make a user object from data given and save it to a database
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


# Logs the user in to the website
@app.route('/login', methods=['GET', 'POST'])
def login() -> json:
    if request.is_json and ("username" and "password" in request.json):
        login_form = request.json

        # Converts json object into dictionary and checks if there are empty
        if empty_values(login_form) == -1:
            return jsonify({
                'status': -1,
                'message': "Login failed: Fill all fields"
            }), 406

        # Finds the user by searching for the username given
        user = User.query.filter_by(username=login_form['username']).first()

        # Checks if the username and password is correct
        if not user or not check_password_hash(user.password, login_form['password']):
            return jsonify({
                'status': -1,
                'message': "Login failed: Username or password is incorrect!"
            }), 406

        # Attempts to create a token to send to front-end with the user logged in data
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


def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in {'png', '.webp', 'jpg', '.jfif',
                                                  '.pjpeg', '.pjp', 'jpeg', 'gif', '.apng'}


@app.route('/submission', methods=['POST'])
@jwt_required()
def submission() -> json:
    current_user = get_jwt_identity()
    if current_user.role != 'user':
        return jsonify({'status': -1,
                        'message': "Unauthorised access attempt"}), 403

    submission_json = request.get_json()
    if "title" and "description" and "postcode" and "date" in submission_json:
        try:
            datetime.datetime.strptime(submission_json["date"], "%m/%d/%y")
        except ValueError as e:
            print(e)
            return jsonify({
                'status': -1,
                'message': "Submission failed: Date is in the wrong format ! "
                           "Should be %m/%d/%y"}), 406

        if 'image' not in request.files or request.files['image'].filename == '':
            return jsonify({
                'status': -1,
                'message': "Submission failed: Image is missing! "}), 406

        image = request.files['image']
        import uuid
        import pathlib
        import os
        if image and allowed_file(image.filename):
            image_name = str(uuid.uuid4()) + pathlib.Path(image.filename).suffix
            file_path = 'api/data/images/' + str(current_user.id) + "/" + str(image_name)
            os.system("mkdir " + '/' + str(current_user.id))
            image.save(file_path)

            complaint = Complaint(title=submission_json["title"],
                                  description=submission_json["description"],
                                  postcode=submission_json["postcode"],
                                  date=submission_json["date"],
                                  user_id=current_user.id,
                                  img_path=file_path)

            db.session.add(complaint)
            db.session.commit()
            return jsonify({
                'status': 0,
                'message': "Submission successful"}), 201
        return jsonify({
            'status': -1,
            'message': "Submission failed: Try again!"}), 406


# Logs the user out of the website
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


# The admin page used to manage complaints
@app.route("/admin", methods=["POST"])
@jwt_required()
def admin() -> json:

    # Checks if the user is an admin
    current_user = get_jwt_identity()
    if current_user.role != 'admin':
        return jsonify({'status': -1,
                        'message': "Unauthorised access attempt"}), 403

    complaints = []
    urls = []
    JSON_complaints = []
    JSON_urls = []

    from sqlalchemy import desc
    quick_search = db.session.query(Complaint.id).order_by(desc(Complaint.id)).limit(20)

    for recent_complaints_id in quick_search:
        complaint = db.session.query(Complaint).filter_by(id=recent_complaints_id[0]).first()
        complaints.append(complaint)

    for complaint in complaints:
        url = str(my_host + ':8000' + complaint.img_path)
        urls.append(url)

    for complaint in complaints:
        JSON_complaint = {'id': complaint.id,
                          'title': complaint.title,
                          'description': complaint.description,
                          'postcode': complaint.postcode,
                          'date': complaint.date}
        JSON_complaints.append(JSON_complaint)

    for url in urls:
        JSON_url = {'url': url}
        JSON_urls.append(JSON_url)

    return jsonify({'status': 0,
                    'list of complaints': JSON_complaints,
                    'list of urls': JSON_urls
                    }), 200


if __name__ == "__main__":
    my_host = "localhost"
    my_port = 5000

    from models import User, Complaint

    app.run(host=my_host, port=my_port, debug=True)
