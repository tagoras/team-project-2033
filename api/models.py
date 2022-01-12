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


class Complaint(db.Model):
    __tablename__ = 'complaints'

    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey(User.id), nullable=False)
    title = db.Column(db.String(100), nullable=False)
    description = db.Column(db.String(200), nullable=False)
    postcode = db.Column(db.String(100), nullable=False)
    date = db.Column(db.String(100), nullable=False)
    img_path = db.Column(db.String(300), nullable=False)

    def __init__(self, user_id, title, description, postcode, date, img_path):
        self.user_id = user_id
        self.title = title
        self.description = description
        self.postcode = postcode
        self.date = date
        self.img_path = img_path


# Initialising the database
def init_db():
    import os
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
                     # postcode=generate_password_hash("NE6 9RU"),
                     postcode="NE1 2AA",
                     role='user')

    test_submission = Complaint(user_id=2,
                                title='Test Submission',
                                description='To use for testing',
                                postcode='NE8 8BC',
                                date='1/5/2022',
                                img_path='data/cats/cat.jpg')

    db.session.add(test_admin)
    db.session.add(test_user)
    db.session.add(test_submission)
    db.session.commit()

    # the code breaks during init_db()
    # Somehow line 98 seems to fail to create a folder and then
    # when it accesses it, the script crashes
    
    # import requests
    # import shutil
    # os.system("mkdir data/cats")
    # url1 = "https://2.bp.blogspot.com/-i5JOdegCL2k/UIUR2YDLauI/AAAAAAAAHwg/yLoHtvi3qKM/\
    #         s1600/close-up_cats_cat_desktop_1920x1200_hd-wallpaper-834709.jpg"
    # res1 = requests.get(url=url1, stream=True)
    # if res1.status_code == 200:
    #     with open("data/cats/cat.jpg", 'wb') as f:
    #         shutil.copyfileobj(res1.raw, f)

    # url2 = "https://welovecatsandkittens.com/wp-content/uploads/2017/01/wiggle.gif"
    # res2 = requests.get(url=url2, stream=True)
    # if res2.status_code == 200:
    #     with open("data/cats/cat.gif", 'wb') as f:
    #         shutil.copyfileobj(res2.raw, f)

    print("init_db successful")
