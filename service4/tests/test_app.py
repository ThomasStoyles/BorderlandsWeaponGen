from application import app
from flask import url_for
from flask_testing import TestCase
import requests_mock


class TestBase(TestCase):
    def create_app(self):
        return app


class TestResponse(TestBase):
    def test_get_damage1(self):
        response = self.client.post(url_for('final'), json={"Manufacturer": "Atlas", "rarity": "Common"})
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'15', response.data)

    def test_get_damage2(self):
        response = self.client.post(url_for('final'), json={"Manufacturer": "Hyperion", "rarity": "Rare"})
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'70', response.data)

    def test_get_damage3(self):
        response = self.client.post(url_for('final'), json={"Manufacturer": "Jakobs", "rarity": "Unknown"})
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'300', response.data)

    def test_get_damage4(self):
        response = self.client.post(url_for('final'), json={"Manufacturer": "Vladof", "rarity": "Legendary"})
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'130', response.data)

    def test_get_damage5(self):
        response = self.client.post(url_for('final'), json={"Manufacturer": "Maliwan", "rarity": "Pearlescent"})
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'195', response.data)

    def test_get_damage6(self):
        response = self.client.post(url_for('final'), json={"Manufacturer": "Anshin", "rarity": "Uncommon"})
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'40', response.data)

    def test_get_damage7(self):
        response = self.client.post(url_for('final'), json={"Manufacturer": "Maliwan", "rarity": "Epic"})
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'95', response.data)