import unittest
# import json
# import os
# import webbrowser

import requests

import app


class FlaskApp(unittest.TestCase):
    def testHello_World(self):
        r = requests.get('http://localhost:5000/hello_world')
        json_content = r.json()
        self.assertEqual(json_content[0], {'title': "Hello!", 'content': "Hello World"})
        self.assertEqual(r.headers['Content-Type'], 'application/json')
        self.assertEqual(r.status_code, 200)
        self.assertEqual(r.url, 'http://localhost:5000/hello_world')

    def testHas_Empty_Value(self):
        d1 = {1: ""}
        d2 = {1: " "}
        d3 = {1: "Hello World", 2: "   "}
        d4 = {1: "Lorem", 2: "Ipsum"}
        self.assertTrue(app.has_empty_value(d1))
        self.assertTrue(app.has_empty_value(d2))
        self.assertTrue(app.has_empty_value(d3))
        self.assertFalse(app.has_empty_value(d4))


if __name__ == '__main__':
    unittest.main()
