import unittest
from unittest import TestCase
from app import create_app, db
from models import Moves
from config import TestConfig

endpoint = "/moves"
class TestMoves(TestCase):
    """Testing Moves table"""

    def setUp(self) -> None:
        """Set up test database"""
        self.app = create_app(TestConfig)
        self.client = self.app.test_client(self)

        with self.app.app_context():
            db.create_all()

    def test_get_move_by_id(self):
        id = 1
        get_response = self.client.get(f"{endpoint}/id/{id}")
        status_code = get_response.status_code
        self.assertEqual(status_code, 404)

    def tearDown(self) -> None:
        """Drop tables"""
        with self.app.app_context():
            db.session.remove()
            db.drop_all()


if __name__ == "__main__":
    unittest.main()
