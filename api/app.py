from flask import Flask, render_template, request, jsonify
from flask_login import LoginManager, current_user
from pymongo import MongoClient
from bson.objectid import ObjectId  # TODO: This is for json pbjects and etc
from flask_cors import CORS
import yaml
import socket


app = Flask(__name__)
config = yaml.load(open('database.yaml'))   # TODO: won't work past this point, database necesssary
client = MongoClient(config['uri'])
# db = client.lin_flask
db = client['knf-dev']
CORS(app)


@app.route('/')
def index():
    return "Hello"


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

    import mysql.connector as database

    USERNAME = "USERNAME"       # TODO: replace with real one
    PASSWORD = "PASSWORD"       # TODO: replace with real one

    connection = database.connect(
        user=USERNAME,
        password=PASSWORD,
        host=my_host,
        database="DATABASE")    # TODO: replace with real one

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


