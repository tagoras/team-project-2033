# IMPORTS
import json
import re
import filetype

from flask import Flask, request, jsonify, send_from_directory
from flask_cors import CORS
from flask_jwt_extended import create_access_token, get_jwt_identity, jwt_required, JWTManager
from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash, check_password_hash
import pyotp

# CONFIG
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data/api.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = 'This is supposed to be a secret key, thank you for your understanding.'
db = SQLAlchemy(app)
CORS(app)

app.config["JWT_SECRET_KEY"] = "Yet again another super secret key, thank you for your understanding."
app.config["JWT_COOKIE_SECURE"] = True
app.config["JWT_TOKEN_LOCATION"] = ["headers", "cookies"]
jwt = JWTManager(app)


# Searches through a dictionary containing a string to see if any key has an empty string

def has_empty_value(obj) -> bool:
    if obj is None:
        return True
    for k in obj:
        t = 0
        for s in str(obj[k]):
            if s == '':
                return True
            elif s == ' ':
                t += 1
            else:
                continue
        if len(str(obj[k])) == t:
            return True
    return False


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
        if has_empty_value(registration_form):
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
        elif password_size > 12 or password_size < 6:
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
        # registration_form['postcode'] = generate_password_hash(registration_form['postcode'])

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

            from mail import Mail

            mail = Mail()
            mail.send_2fa_email(new_user)
            mail.exit()

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
@app.route('/login', methods=['POST'])
def login() -> json:
    if request.is_json and ("username" and "password" and "otp" in request.json):
        login_form = request.json

        # Converts json object into dictionary and checks if there are empty
        if has_empty_value(login_form):
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

        if not pyotp.TOTP(user.otp_key).verify(login_form['otp']):
            print(login_form['otp'])
            print(pyotp.TOTP(user.otp_key).now())
            print(pyotp.TOTP(user.otp_key).verify(login_form['otp']))
            return jsonify({
                'status': -1,
                'message': "Login failed: One Time Password is incorrect!"
            }), 406

        # Attempts to create a token to send to front-end with the user logged in data
        try:
            user = {
                'id': user.id,
                'postcode': user.postcode,
                'username': user.username,
                'email': user.email,
                'role': user.role
            }

            access_token = create_access_token(identity=user)
            return jsonify({
                'status': 0,
                'message': "User successfully logged in",
                'JWT': access_token}), 202
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


# Checks the file type and allow certain ones in
def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in {'.png', '.webp', '.jpg', '.jfif',
                                                  '.pjpeg', '.pjp', '.jpeg', '.gif', '.apng'}


# Allows a logged-in user to submit a complaint which then gets stored in the database
@app.route('/submission', methods=['PUT', 'POST'])
@jwt_required()
def submission() -> json:
    # Grabs the user information and see if they have the role of a user
    current_user = get_jwt_identity()
    if current_user["role"] != 'user':
        return jsonify({'status': -1,
                        'message': "Unauthorised access attempt"}), 403

    user = User.query.filter_by(id=current_user["id"]).first()

    # Checks if submission has passed in any empty fields, if so it will produce error message for front-end
    submission_json = request.get_json()
    print(request.json)
    if has_empty_value(submission_json):
        print(submission_json)
        return jsonify({
            'status': -1,
            'message': "Submission failed: Fill all fields!"
        }), 406

    # Sees if these fields are given by front-end
    if "name" and "description" and "email" and "location" in submission_json:
        # Gets date of when submission is handed in
        import datetime
        dt = datetime.datetime.today()
        month = dt.month
        day = dt.day
        year = dt.year
        date = "{}/{}/{}".format(month, day, year)

        import uuid

        import os
        # See if given file is an image and then saves it to a file and records image path
        # If image isn't allowed produces error

        img_name = str(uuid.uuid4())
        img_path = f'{current_user["id"]}/{img_name}'
        # os.system(f'mkdir data/{current_user["id"]}')

        # Saves the user submission to database into the complaint table
        complaint = Complaint(name=submission_json.get("name"),
                              description=submission_json.get('description'),
                              location=submission_json.get('location'),
                              date=date,
                              user_id=current_user['id'],
                              img_path=img_path,
                              user_key=user.user_key)

        db.session.add(complaint)
        db.session.commit()
        return jsonify({
            'status': 0,
            'message': "Submission successful",
            'submission_id': complaint.id}), 201
    return jsonify({
        'status': -1,
        'message': "Submission failed: Try again!"}), 406


# Images feature didn't make it into the final cut.
@app.route('/submission_file/<int:__id>/<string:__filename>', methods=['PUT', 'POST'])
@jwt_required()
def submission_file(__id, __filename) -> json:
    # Grabs the user information and see if they have the role of a user
    current_user = get_jwt_identity()
    if current_user["role"] != 'user':
        return jsonify({'status': -1,
                        'message': "Unauthorised access attempt"}), 403

    # user = User.query.filter_by(id=current_user["id"]).first()
    complaint = Complaint.query.filter_by(id=__id).first()
    if not complaint:
        return jsonify({
            'status': -1,
            'message': "What is this?"}), 400
    # Checks if submission has passed in any empty fields, if so it will produce error message for front-end
    img = request.get_data()
    import os
    import pathlib
    import filetype
    if img:
        try:
            os.mkdir(f'data/{current_user["id"]}')
        except (FileNotFoundError, FileExistsError) as e:
            print(e)
        file = open("data/" + complaint.img_path, "wb")
        file.write(img)
        extension = pathlib.Path(__filename).suffix
        if filetype.is_image("data/" + complaint.img_path):
            img_path = complaint.img_path + str(extension)
            file.close()
            os.rename("data/" + complaint.img_path, "data/" + img_path)

            db.session.query(Complaint).filter_by(id=complaint.id) \
                .update({Complaint.img_path: img_path})
            db.session.commit()
        # See if given file is an image and then saves it to a file and records image path
        # If image isn't allowed produces error
        return jsonify({
            'status': 0,
            'message': "Submission successful"}), 201
    return jsonify({
        'status': -1,
        'message': "Submission failed: Choose another file"}), 406


# Logs the user out of the website
@app.route("/logout", methods=["GET"])
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
@app.route("/admin/view_all", methods=["POST"])
@jwt_required()
def admin_view_all() -> json:
    # Grabs user info and checks if the user is an admin
    current_user = get_jwt_identity()
    if current_user["role"] != 'admin':
        return jsonify({'status': -1,
                        'message': "Unauthorised access attempt"}), 403

    from sqlalchemy import desc

    # Used to search the database for the biggest ids in complaint id
    quick_search = db.session.query(Complaint.id).order_by(desc(Complaint.id)).limit(100)

    # Puts all the complaints into complaints list
    json_complaints = []

    for complaint in quick_search:
        # Images feature didn't make it into the final cut.
        # Grabs the image urls for each complaint and adds them to the urls list
        url = f'http://{my_host}:5000/file/{complaint.img_path}'
        # Turns all complaints in complaints list to a dictionary and adds them to json complaints list
        user = User.query.filter_by(id=complaint.user_id).first()
        json_complaint = complaint.view_complaint_card(user_key=user.user_key, url=url)
        json_complaints.append(json_complaint)

    # Images feature didn't make it into the final cut.
    # Turns all urls in urls list into a dictionary and adds them to json urls list

    print(json_complaints)

    # Sends the list of complaints and urls to front-end
    return jsonify({'status': 0,
                    'list of complaints': json_complaints,
                    }), 200


# Admin can delete a submission
@app.route("/admin/delete", methods=["DELETE"])
@jwt_required()
def admin_delete_submission() -> json:
    # TODO: ADD PICTURES
    if request.is_json and ("id" in request.json):
        # Checks if the user is an admin
        current_user = get_jwt_identity()

        if current_user["role"] != 'admin':
            return jsonify({'status': -1,
                            'message': "Unauthorised access attempt"}), 403

        # Grabs the id to search for from front-end
        _id = request.json["id"]

        try:
            import os

            # Finds the id in the complaints table
            complaint = db.session.query(Complaint).filter_by(id=_id).first()
            # img_path = complaint.img_path Images feature didn't make it into the final cut.
            db.session.delete(complaint)

            '''
            Images feature didn't make it into the final cut.
            Attempts to find image and delete it
            if os.path.exists(img_path):
                os.system('rm ' + 'data/' + img_path)
                # os.remove('data/'+complaint_image)
            else:
                print("Image and/or path not found")
            '''

            db.session.commit()
            return jsonify({
                'status': 0,
                'message': "Database operation successful"
            }), 201

        except Exception as e:
            print(e)
            return jsonify({
                'status': -1,
                'message': "Database operation failed: Internal error"
            }), 500


# Send the role of the user to front-end
@app.route("/get_role", methods=["GET"])
@jwt_required()
def get_role() -> json:
    # Grabs the logged-in user info
    current_user = get_jwt_identity()
    return jsonify(role=current_user["role"]), 201


# Gets a single file
@app.route('/file/<string:_id>/<string:_filename>', methods=["GET"])
def get_single_file(_id, _filename):
    return send_from_directory(path=f'{_id}/{_filename}', directory="./")


# Admin edits a submission's details
@app.route('/admin/edit', methods=['GET', 'POST'])
@jwt_required()
def admin_edit_submission() -> json:
    current_user = get_jwt_identity()
    # Checks if user is admin
    if current_user["role"] != 'admin':
        return jsonify({'status': -1,
                        'message': "Unauthorised access attempt"}), 403
    # Gets the submission's id from front-end
    submission_id = request.json["submission_id"]

    # Checks if the submissions id given exists in the database
    to_edit = Complaint.query.filter_by(id=submission_id).first()
    if to_edit and not has_empty_value(request.json):
        # Changes the submission details with the details given by front-end
        db.session.query(Complaint).filter_by(id=submission_id) \
            .update({Complaint.name: request.json["submission_name"],
                     Complaint.description: request.json["submission_description"],
                     Complaint.location: request.json["submission_location"],
                     Complaint.date: request.json["date"]})

        db.session.commit()

        return jsonify({'status': 0,
                        'message': 'Submission edited'}), 201
    else:
        return jsonify({'status': -1,
                        'message': 'ID Incorrect, try again'}), 406


if __name__ == "__main__":
    my_host = "localhost"
    my_port = 5000

    from models import User, Complaint

    app.run(host=my_host, port=my_port, debug=True)
