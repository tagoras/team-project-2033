import unittest
# import json
# import os

import requests

import app


class FlaskApp(unittest.TestCase):

    """
        def __init__(self, JWT='', ADMIN_JWT=''):
            super().__init__()
            self.JWT = JWT
            self.ADMIN_JWT = ADMIN_JWT
    """


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
        r = requests.get('http://localhost:5000/hello_world', stream=True)
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
        r = requests.post(url=url, json=data, stream=True)
        self.assertEqual(406, r.status_code)

        data = {'username': 'Test',
                'email': 'Test@example.com',
                'postcode': 'A bad postcode :(',
                'password': 'He110 w0r1d£'}
        r = requests.post(url=url, json=data, stream=True)
        self.assertEqual(406, r.status_code)

        data = {'username': 'Test',
                'email': 'Test@example.com',
                'postcode': 'NE2 5RE',
                'password': 'A not so good password :('}
        r = requests.post(url=url, json=data, stream=True)
        self.assertEqual(406, r.status_code)

        data = {'username': 'Test',
                'email': 'Test@example.com',
                'postcode': 'NE2 5RE',
                'password': 'He110 w0r1d£'}
        r = requests.post(url=url, json=data, stream=True)
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
        r = requests.post(url=url, json=login_data, stream=True)
        self.assertEqual(406, r.status_code)

        login_data = {'username': 'Test',
                      'password': 'A not so good password :('}
        r = requests.post(url=url, json=login_data, stream=True)
        self.assertEqual(406, r.status_code)

        """        
        login_data = {'username': 'Test',
                      'password': 'He110 w0r1d£'}
        r = requests.post(url=url, json=login_data)
        self.assertEqual(202, r.status_code)

        jwt = r.json()[0]['JWT']
        print(jwt)
        self.JWT = jwt
        """
        login_data = {'username': 'Joe',
                      'password': 'Njdka3rq39h!'}
        r = requests.post(url=url, json=login_data, stream=True)
        self.assertEqual(202, r.status_code)

        admin_jwt = r.json()['JWT']
        print(admin_jwt)
        self.ADMIN_JWT = admin_jwt

    def test_get_single_file(self):
        import webbrowser

        url1 = 'http://localhost:5000/file/cats/cat.gif'
        url2 = 'http://localhost:5000/file/cats/cat.jpg'

        webbrowser.open_new_tab(url1)
        webbrowser.open_new_tab(url2)

        status_code = requests.get(url=url1, stream=True).status_code
        self.assertEqual(200, status_code)

        status_code = requests.get(url=url2, stream=True).status_code
        self.assertEqual(200, status_code)


if __name__ == '__main__':
    unittest.main()
