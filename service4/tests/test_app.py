from flask import Flask, url_for
from flask_testing import TestCase
import application.routes
from application import app 
from unittest.mock import patch


class TestBase(TestCase):
    def create_app(self):
        return app


class TestResponse(TestBase):

    def test_get_manufacturer(self):

        for i in Manufacturers:
            for j in range(105):

                content = {'Manufacturers':i, 'rarity':j}
                response = self.client.post(url_for('post_status'), json=content)

                self.assert200(response)

                if j <= 30:
                    self.assertIn("Common", response.data.decode())
                elif j <= 55:
                    self.assertIn("Uncommon", response.data.decode())
                elif j <= 75:
                    self.assertIn("Rare", response.data.decode())
                elif j <= 90:
                    self.assertIn("Epic", response.data.decode())
                elif j <= 100:
                    self.assertIn("Legendary", response.data.decode())
                else:
                    self.assertIn("Unknown", response.data.decode())