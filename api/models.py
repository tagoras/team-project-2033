# IMPORTS

import base64

from app import db

from Crypto.Protocol.KDF import scrypt
from Crypto.Random import get_random_bytes
from cryptography.fernet import Fernet
from flask_login import UserMixin
from werkzeug.security import generate_password_hash


def encrypt(data, key):
    return Fernet(key).encrypt(bytes(data, 'utf-8'))


def decrypt(data, key):
    return Fernet(key).decrypt(data).decode('utf-8')


# User Table
class User(db.Model, UserMixin):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(100), nullable=False, unique=True)
    password = db.Column(db.String(200), nullable=False)
    email = db.Column(db.String(100), nullable=False)
    postcode = db.Column(db.String(100), nullable=False)
    role = db.Column(db.String(10), nullable=False)
    user_key = db.Column(db.BLOB)
    otp_key = db.Column(db.String(100), nullable=False)

    # Initialise User Object
    def __init__(self, username, email, password, postcode, role):
        self.username = username
        self.email = email
        self.password = password
        self.postcode = postcode
        self.role = role
        self.user_key = base64.urlsafe_b64encode(scrypt(password, str(get_random_bytes(32)), 32, N=2 ** 14, r=8, p=1))
        self.otp_key = base64.b32encode(get_random_bytes(20))


class Complaint(db.Model):
    __tablename__ = 'complaints'

    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey(User.id), nullable=False)
    name = db.Column(db.String(100), nullable=False)
    description = db.Column(db.String(200), nullable=False)
    location = db.Column(db.String(200), nullable=False)
    date = db.Column(db.String(15), nullable=False)
    img_path = db.Column(db.String(300), nullable=False)

    # Initialise Complaint Object
    def __init__(self, user_id, name, description, location, date, img_path, user_key):
        self.user_id = user_id
        self.name = encrypt(data=name, key=user_key)
        self.description = encrypt(data=description, key=user_key)
        self.location = encrypt(data=location, key=user_key)
        self.date = encrypt(data=date, key=user_key)
        self.img_path = img_path
        db.session.commit()

    def view_complaint_card(self, user_key, url):
        # self.name = decrypt(data=self.name, key=user_key)
        # self.description = decrypt(data=self.description, key=user_key)
        # self.location = decrypt(data=self.location, key=user_key)
        # self.date = decrypt(data=self.date, key=user_key)
        return {
            'name': decrypt(data=self.name, key=user_key),
            'description': decrypt(data=self.description, key=user_key),
            'location': decrypt(data=self.location, key=user_key),
            'date': decrypt(data=self.date, key=user_key),
            'id': self.id,
            'user_id': self.user_id,
            'url': url

        }
        # self.img_path = decrypt(data=self.img_path, key=user_key) Images feature didn't make it into the final cut.


# Initialising the database
def init_db():
    import os
    import shutil
    print("running init_db...")
    # Deletes the folder and creates it again
    os.system("rm -rf data && mkdir data")

    db.drop_all()
    db.create_all()

    test_admin = User(username='Joe',
                      email='test1@test.com',
                      password=generate_password_hash('Njdka3rq39h!'),
                      # postcode=generate_password_hash("NE6 9RU"),
                      postcode="NE6 9RU",
                      role='admin')

    test_user = User(username='Steve',
                     email='Steve@test.com',
                     password=generate_password_hash('Pass123!'),
                     # postcode=generate_password_hash("NE6 9RU"), Images feature didn't make it into the final cut.
                     postcode="NE1 2AA",
                     role='user')

    test_submission = Complaint(user_id=2,
                                name='Test Submission',
                                description='To use for testing',
                                location='21, North but south of Haymarket but not like, right right there',
                                date='1/5/2022',
                                img_path='cats/cat.gif',
                                user_key=test_user.user_key)

    db.session.add(test_admin)
    db.session.add(test_user)
    db.session.add(test_submission)
    db.session.commit()

    import requests
    import shutil
    # Creates a folder in data called cats
    os.makedirs("data/cats")
    # Downloads an image from the internet
    url1 = "https://amolife.com/image/Pictures_of_Cute_Cats_7.jpg"
    res1 = requests.get(url=url1, stream=True)
    if res1.status_code == 200:
        with open("data/cats/cat.jpg", 'wb') as f:
            shutil.copyfileobj(res1.raw, f)

    # Downloads a gif from the internet
    url2 = "https://welovecatsandkittens.com/wp-content/uploads/2017/01/wiggle.gif"
    res2 = requests.get(url=url2, stream=True)
    if res2.status_code == 200:
        with open("data/cats/cat.gif", 'wb') as f:
            shutil.copyfileobj(res2.raw, f)

    print("init_db successful")
