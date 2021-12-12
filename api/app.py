from flask import Flask, render_template, request, jsonify
from flask_login import LoginManager, current_user
from pymongo import MongoClient
from bson.objectid import ObjectId  # will be useful in the future
from flask_cors import CORS
import socket
import json
from werkzeug.security import generate_password_hash
import re

app = Flask(__name__)

# won't work past this point if not run on uni machines
# client = MongoClient('mongodb://cs-db.ncl.ac.uk:3306/csc2033_team32')
# db = client['csc2033_team32']
CORS(app)


def empty_values(dictionary):
    for key in dictionary:
        if dictionary[key] == '':
            return 'Empty'
    return 0


@app.route('/')
def hello_world():
    return "<p>Hello, World!</p>"


@app.route('/register2', methods=['GET', 'POST'])
def register():
    # POST a data to database
    if request.method == 'POST':
        body = request.form.get
        print(json.loads(body))
        
    return "empty"

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
    # TODO: Save this to db in the users table and check if username is taken and return true or false to front end


@app.route('/login')
def login(user_info):
    user_dictionary = json.loads(user_info)
    password = user_dictionary["password"]
    user_dictionary["password"] = decrypt_password(password)
    user_info = json.dumps(user_dictionary)
    return user_info
    # TODO: Understand what any of this actually means or does, just trying to be helpful guys xx


if __name__ == "__main__":
    my_host = "localhost"
    # TODO: the free socket thing should be replaced with a unique socket if deployed in uni's VMs
    free_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    free_socket.bind((my_host, 0))
    free_socket.listen(5)
    free_port = free_socket.getsockname()[1]
    free_socket.close()

    login_manager = LoginManager()
    login_manager.login_view = 'users.login'
    login_manager.init_app(app)

    ''' Commented to avoid errors
    import mysql.connector as database

    USERNAME = input("Database username: ")
    PASSWORD = input("Database password: ")

    connection = database.connect(
        user=USERNAME,
        password=PASSWORD,
        host='cs-db.ncl.ac.uk',
        database="csc2033_team32")

    cursor = connection.cursor()


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


    app.run(host=my_host, port=free_port, debug=True, ssl_context='adhoc')
    # TODO : add connection.close() at the end of program for the database
    '''
