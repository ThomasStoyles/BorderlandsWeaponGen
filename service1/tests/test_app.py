from flask import Flask, url_for
from flask_testing import TestCase
import application.routes
from application import app 
from unittest.mock import patch
import requests_mock

class TestBase(TestCase):
    def create_app(self):
        return app

#Testing the route index
class Testindex(TestBase):
    def test_get_index(self):
            response =self.client.get(url_for('index'))
            self.assert500(response)

#Test gun 1
class TestGun1(TestBase):
    def test_gun1(self):
        with requests_mock.Mocker() as m:
            m.get('http://service2:5000/Manufacturer', text='Jakobs')
            m.get('http://service3:5000/rarity',text='47')
            m.post('http://service4:5000/final', json={
        'Weapon Type': 'Jakobs',
        'Weapon rarity': 'Rare',
        'damage type on weapon': 'Ice'
        })

        response = self.client.get(url_for('index'))
        self.assert500(response)
        self.assertIn(b'Weapon Type: Jakobs', response.data.decode)

