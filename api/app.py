from flask import Flask, render_template, request, jsonify
from flask_login import LoginManager, current_user
from pymongo import MongoClient
from bson.objectid import ObjectId  # will be useful in the future
from flask_cors import CORS
import socket
import json
from werkzeug.security import generate_password_hash

app = Flask(__name__)

# won't work past this point if not run on uni machines
# client = MongoClient('mongodb://cs-db.ncl.ac.uk:3306/csc2033_team32')
# db = client['csc2033_team32']
CORS(app)


@app.route('/')
def hello_world():
    return "<p>Hello, World!</p>"


@app.route('/register')
def register(user_info):
    user_dictionary = json.loads(user_info)
    password = user_dictionary["password"]
    postcode = user_dictionary["postcode"]
    user_dictionary["password"] = generate_password_hash(password)
    user_dictionary["postcode"] = generate_password_hash(postcode)
    user_info = json.dumps(user_dictionary)
    return user_info
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
