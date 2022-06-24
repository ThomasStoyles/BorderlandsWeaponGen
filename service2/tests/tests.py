from flask import Flask
from flask_testing import TestCase
from app import app,weapons

class TestBase(TestCase):
    def create_app(self)
    return app 

class TestWeapons(TestBase):
    def test_weapon_choice(self):
        for i in range(15):
            response = self.client.get(url_for('weapon_choice'))

            self.assert200(response)
            self.assertIn(response.data(), weapons)
