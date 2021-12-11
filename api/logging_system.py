import csv
import json
import re
from werkzeug.security import generate_password_hash


def empty_values(dictionary):
    for key in dictionary:
        if dictionary[key] == '':
            return -1
    return 0


def registration(reg_info):
    # Converts JSON object into dictionary
    reg_dictionary = json.loads(reg_info)

    # Any empty values
    if empty_values(reg_dictionary) == -1:
        return 'Empty Fields'

    # Username Exists?, Temporarily using csv document
    with open('tempDB.csv', 'r') as f:
        reader = csv.reader(f)
        for row in reader:
            if row[0] == reg_dictionary['username']:
                f.close()
                return 'Username Exists Already'
        f.close()

    # Password Validating
    password_size = len(reg_dictionary['password'])
    password_checker = re.compile(r'([A-Z])+([a-z])+(.\d)+([*?!^+%&()=}{$#@<>])')
    if not (password_checker.match(reg_dictionary['password'])):
        return 'Failed Password validation'
    elif not (6 < password_size < 12):
        return 'Failed Password validation'

    # Email Validating
    regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
    if not re.search(regex, reg_dictionary['email']):
        return 'Failed Email Validation'

    # Postcode Validation
    regex = r'[A-Z]{1,2}[0-9R][0-9A-Z]? [0-9][A-Z]{2}'
    if not re.search(regex, reg_dictionary['postcode']):
        return 'Failed Postcode Validation'

    # One way encrypt
    reg_dictionary["password"] = generate_password_hash(reg_dictionary["password"])
    reg_dictionary["postcode"] = generate_password_hash(reg_dictionary["postcode"])

    # Save to database, temporarily saved to csv document
    with open('tempDB.csv', 'a') as f:
        writer = csv.DictWriter(f, reg_dictionary.keys())
        writer.writerow(reg_dictionary)
        f.close()

    # Converts back into JSON object
    user_info = json.dumps(reg_dictionary)

    # Returns user_info
    return 'User Registered Successfully'
    # TODO: Save user_info to db


def login(login_info):
    # Converts JSON object into dictionary
    login_dictionary = json.loads(login_info)

    # Any empty values
    if empty_values(login_dictionary) == -1:
        return 'Empty Fields'

    f = open("tempDB.txt", 'r')
    # TODO: f = READ FILE !!!!

    # Converts back into JSON object
    user_info = json.dumps(login_dictionary)

    # Save to database, temporarily saved to text document
    f = open("tempDB.txt", 'a')
    f.write(user_info)
    f.close()

    # Returns user_info
    return 'User Logged In Successfully'
