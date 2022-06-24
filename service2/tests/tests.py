from flask import Flask
from flask_testing import TestCase
from application.routes import app, Manufacturer

class TestBase(TestCase):
    def create_app(self)
    return app 

class TestManufacturer(TestBase):
    def test_Manufacturer(self):
        for i in range(15):
            response = self.client.get(url_for('Manufacturer_choice'))

            self.assert200(response)
            self.assertIn(response.data(), Manufacturer)
