from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager, current_user
from flask_cors import CORS
import json
from werkzeug.security import generate_password_hash
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
    # just for testing : return an hello world json object, for debbugging api calls
    return {'title': "Hello!",
            'content': "Hello World"}


#   TODO: Rewrite all of this to reflect the database change
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


'''
def Hello(reg_info):
    # Converts JSON object into dictionary
    reg_dictionary = json.loads(reg_info)

    # Any empty values
    if empty_values(reg_dictionary) == -1:
        return -1

    # Password Validating
    password_size = len(reg_dictionary['password'])
    password_checker = re.compile(r'(?=.*\d)(?=.*[a-z])(?=.*[A-Z])(?=.*[*?!^+%&()=}{$#@<>])')
    if password_checker.match(reg_dictionary['password']):
        return 'Failed Password validation'
    elif 6 > password_size and 12 > password_size:
        return 'Failed Password validation'

    # Email Validating
    regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
    if not re.search(regex, reg_dictionary['email']):
        return 'Failed Email Validation'

    # Postcode Validation
    regex = r'[A-Z]{1,2}[0-9R][0-9A-Z]? [0-9][A-Z]{2}'
    if not re.search(regex, reg_dictionary['postcode']):
        return -1

    # One way encrypt
    reg_dictionary["password"] = generate_password_hash(reg_dictionary["password"])
    reg_dictionary["postcode"] = generate_password_hash(reg_dictionary["postcode"])

    # Converts back into JSON object
    user_info = json.dumps(reg_dictionary)

    f = open("tempDB.txt", 'a')
    f.write(user_info)
    f.close()

    # Returns user_info
    return 0
'''


@app.route('/login')
def login(user_info):
    user_dictionary = json.loads(user_info)
    password = user_dictionary["password"]
    user_dictionary["password"] = decrypt_password(password)
    user_info = json.dumps(user_dictionary)
    return user_info
    # TODO: Understand what any of this actually means or does, just trying to be helpful guys xx


if __name__ == "__main__":
    from models import User
    my_host = "localhost"
    my_port = 5000

    '''Commented to avoid errors
    login_manager = LoginManager()
    login_manager.login_view = 'users.login'
    login_manager.init_app(app)
    
    @login_manager.user_loader
    def load_user(username):
        try:
            statement = "SELECT username FROM Users WHERE username=%s"
            user = (username,)
            cursor.execute(statement, user)
            return user
        except db.Error as e:
            print("load_user failed\n" + e)
            return -1
    '''
    app.run(host=my_host, port=my_port, debug=True)
