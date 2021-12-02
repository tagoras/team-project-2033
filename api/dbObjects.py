from werkzeug.security import generate_password_hash


class user:

    def __init__(self, username, password, email, postcode):
        self.username = username
        self.password = generate_password_hash(password)
        self.email = email
        self.postcode = postcode
        # TODO: Need to be able to encrypt and decrypt postcode
