import unittest
from flask import Flask
from app import app

class TestHelloWorld(unittest.TestCase):

    def setUp(self):
        self.app = app.test_client()

    def test_index_page(self):
        response = self.app.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Welcome to Unit Testing', response.data)

if __name__ == '__main__':
    unittest.main()
