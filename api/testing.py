import unittest
# import json
# import os
# import webbrowser

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


if __name__ == '__main__':
    unittest.main()
