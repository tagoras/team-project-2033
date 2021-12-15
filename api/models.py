import os
from app import db


class User(db.Model):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(100), nullable=False, unique=True)
    password = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100), nullable=False)
    postcode = db.Column(db.String(100), nullable=False)

    def __init__(self, username, email, password, postcode):
        self.username = username
        self.email = email
        self.password = password
        self.postcode = postcode


def init_db():
    try:
        print("running init_db...")
        os.system("mkdir data")
    except OSError as e:
        print("data/ already exists: ")
        print(e)

    db.drop_all()
    db.create_all()
    test_user = User(username='Joe', email='test1@test.com', password='Njdka3rq39h!', postcode="NE6 9RU")
    db.session.add(test_user)
    db.session.commit()
