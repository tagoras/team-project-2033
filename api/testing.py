import unittest
import json
# import os

import requests

import app


class FlaskApp(unittest.TestCase):


    def test_has_empty_value(self):
        d1 = {1: ""}
        d2 = {1: " "}
        d3 = {1: "Hello World", 2: "   "}
        d4 = {1: "Lorem", 2: "Ipsum"}
        self.assertTrue(app.has_empty_value(d1))
        self.assertTrue(app.has_empty_value(d2))
        self.assertTrue(app.has_empty_value(d3))
        self.assertFalse(app.has_empty_value(d4))


    def test_hello_world(self):
        r = requests.get('http://localhost:5000/hello_world')
        json_content = r.json()
        print(json_content)
        self.assertEqual({'title': "Hello!", 'content': "Hello World"}, json_content[0])
        self.assertEqual('application/json', r.headers['Content-Type'], )
        self.assertEqual(200, r.status_code, )
        self.assertEqual('http://localhost:5000/hello_world', r.url, )

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


if __name__ == '__main__':
    unittest.main()
