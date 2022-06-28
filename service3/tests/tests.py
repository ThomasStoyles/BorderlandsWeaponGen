from application import app 
import application.routes
from flask_testing import TestCase

class TestBase(TestCase):
    def create_app(self):
        return app


class TestRarity(TestBase):
    @patch('application.routes.randint', return_value=123456789)
    def test_numbs(self, patched):
        response = self.client.get(url_for('rarity'))
        self assert200(response)
        self.assertIn(b'123456789', response.data)

    @patch('application.routes.randint', return_value=987654321)
    def test_numbsV2(self, patched):
        response = self.client.get(url_for('rarity'))
        self assert200(response)
        self.assertIn(b'987654321', response.data)