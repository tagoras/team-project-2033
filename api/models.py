# IMPORTS
try:
    from app import db
except ModuleNotFoundError:
    import os

    print("\033[1;31m\nYou're running python inside the wrong directory...")
    print("Please make sure console is running inside \033[1;93mapi\033[1;31m and not \033[1;93m" +
          os.path.basename(os.getcwd()))
    print("\033[1;31m\nAborting so no permanent damage is done...")
    exit(-1)
from flask_login import UserMixin
from werkzeug.security import generate_password_hash


# User Table
class User(db.Model, UserMixin):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(100), nullable=False, unique=True)
    password = db.Column(db.String(200), nullable=False)
    email = db.Column(db.String(100), nullable=False)
    postcode = db.Column(db.String(100), nullable=False)
    role = db.Column(db.String(10), nullable=False)

    # Initialise User Object
    def __init__(self, username, email, password, postcode, role):
        self.username = username
        self.email = email
        self.password = password
        self.postcode = postcode
        self.role = role


# Initialising the database
def init_db():
    import os
    print("running init_db...")
    # Deletes the folder and creates it again
    os.system("rm -rf data && mkdir data")

    db.drop_all()
    db.create_all()

    test_user = User(username='Joe',
                     email='test1@test.com',
                     password=generate_password_hash('Njdka3rq39h!'),
                     postcode=generate_password_hash("NE6 9RU"),
                     role='admin')

    db.session.add(test_user)
    db.session.commit()
    print("init_db successful")
