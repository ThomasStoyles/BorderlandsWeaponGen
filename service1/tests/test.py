from application import app
from flask_testing import TestCase
from flask import url_for
import requests_mock

class TestBase(TestCase):
    def create_app(self):
        return app

class TestResponse(TestBase):

    def test_index(self):
        requests_mock.get('http://service2:5000/Manufacturer', text='Jakobs')
        requests_mock.get('http://service3:5000/rarity',text='87')
        requests_mock.post('http://service4:5000/final', json={
        
        'Weapon Type': 'Jakobs',
        'Weapon rarity': 'Rare',
        'damage type on weapon': 'Ice'
        })
    
        response = self.client.get(url_for('index'))
    self.assert200(response)

