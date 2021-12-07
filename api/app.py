from flask import Flask, render_template, request, jsonify
from flask_login import LoginManager, current_user
from pymongo import MongoClient
from bson.objectid import ObjectId  # will be useful in the future
from flask_cors import CORS
import socket
import logging_system

app = Flask(__name__)

# won't work past this point if not run on uni machines
# client = MongoClient('mongodb://cs-db.ncl.ac.uk:3306/csc2033_team32')
# db = client['csc2033_team32']
CORS(app)


@app.route('/')
def hello_world():
    return "<p>Hello, World!</p>"


@app.route('/register2', methods=['GET', 'POST'])
def register():
    # Receive data from register form
    if request.method == 'POST':
        user_input = request.data

    # TODO: Return Something for front-end to know what's happened to user input
    return logging_system.registration(user_input)


@app.route('/login', methods=['GET', 'POST'])
def login():
    # Receive data from login form
    if request.method == 'POST':
        user_input = request.data

    # TODO: Return Something for front-end to know what's happened to user input
    return logging_system.login(user_input)


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
