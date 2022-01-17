import unittest
import json
# import os

import requests

import app


class FlaskApp(unittest.TestCase):

    # Tests if has_empty_value function works
    def test_has_empty_value(self):
        d1 = {1: ""}
        d2 = {1: " "}
        d3 = {1: "Hello World", 2: "   "}
        d4 = {1: "Lorem", 2: "Ipsum"}
        self.assertTrue(app.has_empty_value(d1))
        self.assertTrue(app.has_empty_value(d2))
        self.assertTrue(app.has_empty_value(d3))
        self.assertFalse(app.has_empty_value(d4))

    # Tests if hello_world function works
    def test_hello_world(self):
        r = requests.get('http://localhost:5000/hello_world')
        json_content = r.json()
        print(json_content)
        self.assertEqual({'title': "Hello!", 'content': "Hello World"}, json_content[0])
        self.assertEqual('application/json', r.headers['Content-Type'], )
        self.assertEqual(200, r.status_code, )
        self.assertEqual('http://localhost:5000/hello_world', r.url, )

    # Tests the logging out of the user
    def test_logout(self):
        url = 'http://localhost:5000/login'

        login_data = {'username': 'Test',
                      'password': 'He110 w0r1d£'}
        r = requests.post(url=url, json=login_data)
        self.assertEqual(202, r.status_code)

        jwt = r.json()['JWT']
        print(jwt)

        url = 'http://localhost:5000/logout'
        headers = {
            "Authorization": f"Bearer {jwt}",
        }

        r = requests.get(url=url, headers=headers)
        self.assertEqual(200, r.status_code)

        url = 'http://localhost:5000/login'

        login_data = {'username': 'Joe',
                      'password': 'Njdka3rq39h!'}
        r = requests.post(url=url, json=login_data)
        self.assertEqual(202, r.status_code)

        jwt = r.json()['JWT']
        print(jwt)

        url = 'http://localhost:5000/logout'
        headers = {
            "Authorization": f"Bearer {jwt}",
        }

        r = requests.get(url=url, headers=headers)
        self.assertEqual(200, r.status_code)

    # Tests the registering of a user
    def test_register(self):
        url = 'http://localhost:5000/register'

        data = {'username': 'Test',
                'email': 'An incorrect email :(',
                'postcode': 'NE2 5RE',
                'password': 'He110 w0r1d£'}
        r = requests.post(url=url, json=data)
        self.assertEqual(406, r.status_code)

        data = {'username': 'Test',
                'email': 'Test@example.com',
                'postcode': 'A bad postcode :(',
                'password': 'He110 w0r1d£'}
        r = requests.post(url=url, json=data)
        self.assertEqual(406, r.status_code)

        data = {'username': 'Test',
                'email': 'Test@example.com',
                'postcode': 'NE2 5RE',
                'password': 'A not so good password :('}
        r = requests.post(url=url, json=data)
        self.assertEqual(406, r.status_code)

        data = {'username': 'Test',
                'email': 'Test@example.com',
                'postcode': 'NE2 5RE',
                'password': 'He110 w0r1d£'}
        r = requests.post(url=url, json=data)
        self.assertEqual(201, r.status_code)

    # Tests the logging in of a user
    def test_login(self):
        url = 'http://localhost:5000/login'

        login_data = {'username': 'An incorrect username',
                      'password': 'He110 w0r1d£'}
        r = requests.post(url=url, json=login_data, stream=True)
        self.assertEqual(406, r.status_code)

        login_data = {'empty_fields_perhaps': ':(',
                      'username': '',
                      'password': ''}
        r = requests.post(url=url, json=login_data)
        self.assertEqual(406, r.status_code)

        login_data = {'username': 'Test',
                      'password': 'A not so good password :('}
        r = requests.post(url=url, json=login_data)
        self.assertEqual(406, r.status_code)

        login_data = {'username': 'Test',
                      'password': 'He110 w0r1d£'}
        r = requests.post(url=url, json=login_data)
        self.assertEqual(202, r.status_code)

        jwt = r.json()['JWT']
        print(jwt)
        JWT = jwt

        login_data = {'username': 'Joe',
                      'password': 'Njdka3rq39h!'}
        r = requests.post(url=url, json=login_data)
        self.assertEqual(202, r.status_code)

        admin_jwt = r.json()['JWT']
        print(admin_jwt)
        ADMIN_JWT = admin_jwt

    # Tests the getting a single file
    def test_get_single_file(self):
        import webbrowser

        url1 = 'http://localhost:5000/file/cats/cat.gif'
        url2 = 'http://localhost:5000/file/cats/cat.jpg'

        webbrowser.open_new_tab(url1)
        webbrowser.open_new_tab(url2)

        status_code = requests.get(url=url1).status_code
        self.assertEqual(200, status_code)

        status_code = requests.get(url=url2).status_code
        self.assertEqual(200, status_code)

    # Tests the adding of submissions from a user
    def test_submission(self):
        url = 'http://localhost:5000/login'
        login_data = {'username': 'Test',
                      'password': 'He110 w0r1d£'}
        r = requests.post(url=url, json=login_data)
        self.assertEqual(202, r.status_code)

        jwt = r.json()['JWT']

        url2 = "http://localhost:5000/submission"
        submission = {
            "title": "This is a title",
            "description": "This is a very good description",
            "postcode": "NE6 6BA",
            "date": "02/12/02",

        }
        headers = {
            "Authorization": f"Bearer {jwt}",
            'Connection': 'close'
        }
        files = {
            "image": open("data/cats/cat.jpg", "rb")
        }

        r2 = requests.put(url=url2, json=submission, headers=headers, stream=True, files=files)

        print(r2.text)
        print(submission)
        print(r2.request.headers)
        self.assertEqual(201, r2.status_code)

    # Tests if the admin can see 20 of the largest ids
    def test_admin_view_all(self):
        url = 'http://localhost:5000/login'

        login_data = {'username': 'Joe',
                      'password': 'Njdka3rq39h!'}
        r = requests.post(url=url, json=login_data)

        self.assertEqual(202, r.status_code)

        url = 'http://localhost:5000/admin/view_all'

        jwt = r.json()['JWT']
        headers = {
            "Authorization": f"Bearer {jwt}",
            'Connection': 'close'
        }
        r = requests.post(url=url, headers=headers)

        self.assertEqual(200, r.status_code)

    # Tests if the admin can delete a users submission
    def test_admin_delete_submission(self):
        url = 'http://localhost:5000/login'

        login_data = {'username': 'Joe',
                      'password': 'Njdka3rq39h!'}
        r = requests.post(url=url, json=login_data)

        self.assertEqual(202, r.status_code)

        url = 'http://localhost:5000/admin/delete'

        jwt = r.json()['JWT']
        headers = {"Authorization": f"Bearer {jwt}",
                   "Connection": 'close'}
        body = {"id": 1}
        r = requests.delete(url=url, headers=headers, json=body)

        self.assertEqual(201, r.status_code)

        r = requests.delete(url=url, headers=headers, json=body)

        self.assertEqual(500, r.status_code)

    # Tests if front-end can get the role of the current user
    def test_get_role(self):

        url = 'http://localhost:5000/login'
        user = {'username': 'Steve',
                'password': 'Pass123!'}
        r = requests.post(url=url, json=user)

        self.assertEqual(202, r.status_code)
        jwt = r.json()['JWT']

        url = 'http://localhost:5000/get_role'
        header = {"Authorization": f"Bearer {jwt}",
                  'Connection': 'close'}
        r = requests.get(url=url, headers=header)

        self.assertEqual(201, r.status_code)
        self.assertEqual('user', r.json()['role'])

        url = 'http://localhost:5000/login'
        user = {'username': 'Joe',
                'password': 'Njdka3rq39h!'}
        r = requests.post(url=url, json=user)

        self.assertEqual(202, r.status_code)
        jwt = r.json()['JWT']

        url = 'http://localhost:5000/get_role'
        header = {"Authorization": f"Bearer {jwt}",
                  'Connection': 'close'}
        r = requests.get(url=url, headers=header)

        self.assertEqual(201, r.status_code)
        self.assertEqual('admin', r.json()['role'])

    # Tests if the admin can see the next 20 submissions
    def test_admin_next_page(self):

        url = 'http://localhost:5000/login'
        user = {'username': 'Steve',
                'password': 'Pass123!'}
        r = requests.post(url=url, json=user)
        self.assertEqual(202, r.status_code)
        jwt = r.json()['JWT']
        headers = {"Authorization": f"Bearer {jwt}",
                   'Connection': 'close'}

        url = 'http://localhost:5000/admin/search'
        complaint_id = {'complaint_id': 2}
        r = requests.post(url=url, headers=headers, json=complaint_id)

        self.assertEqual(403, r.status_code)

        url = 'http://localhost:5000/login'
        admin = {'username': 'Joe',
                 'password': 'Njdka3rq39h!'}
        r = requests.post(url=url, json=admin)

        self.assertEqual(202, r.status_code)
        jwt = r.json()['JWT']
        headers = {"Authorization": f"Bearer {jwt}",
                   'Connection': 'close'}

        url = 'http://localhost:5000/admin/search'
        complaint_id = {'complaint_id': 2}
        r = requests.post(url=url, headers=headers, json=complaint_id)

        self.assertEqual(200, r.status_code)
        self.assertEqual('Go to admin_view_all function', r.json()['message'])

        url = 'http://localhost:5000/admin/search'
        complaint_id = {'complaint_id': 1}
        r = requests.post(url=url, headers=headers, json=complaint_id)

        self.assertEqual(200, r.status_code)
        self.assertEqual('End of Complaints', r.json()['message'])

    # Tests if the admin can edit a submission in the complaints table
    def test_admin_edit_submission(self):

        url = 'http://localhost:5000/login'
        login_admin = {'username': 'Joe',
                       'password': 'Njdka3rq39h!'}
        r = requests.post(url=url, json=login_admin)

        self.assertEqual(202, r.status_code)
        jwt = r.json()['JWT']
        headers = {"Authorization": f"Bearer {jwt}",
                   'Connection': 'close'}

        url = 'http://localhost:5000/admin/edit'
        complaint_id = {'submission_id': 1,
                        'submission_name': 'Checkpoint 1',
                        'submission_description': 'Checkpoint 2',
                        'submission_x_coord': 3,
                        'submission_y_coord': 4,
                        'date': '01/13/2022'}
        r = requests.post(url=url, headers=headers, json=complaint_id)

        self.assertEqual(201, r.status_code)
        self.assertEqual('Submission edited', r.json()['message'])

        complaint_id = {'submission_id': 102,
                        'submission_name': 'Checkpoint 5',
                        'submission_description': 'Checkpoint 6',
                        'submission_x_coord': 7,
                        'submission_y_coord': 8,
                        'date': '01/13/2022'}
        r = requests.post(url=url, headers=headers, json=complaint_id)

        self.assertEqual(406, r.status_code)
        self.assertEqual('ID Incorrect, try again', r.json()['message'])


if __name__ == '__main__':
    unittest.main()
