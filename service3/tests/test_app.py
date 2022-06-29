from flask import Flask, url_for
from flask_testing import TestCase
import application.routes
from application import app 
from unittest.mock import patch

class TestBase(TestCase):
    def create_app(self):
        return app 

class Testrarity(TestBase):
    @patch('application.routes.rd.choice', return_value='Jakobs')
    def test_mrarity(self, patched):
        response =self.client.get(url_for('rarity'))
        self.assert200(response)
        self.assertIn(b'Jakobs', response.data)