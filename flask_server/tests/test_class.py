import unittest
from unittest import TestCase
from app import create_app, db
from models import Moves, ModuleOne, ModuleTwo, SparringCombination
from config import TestConfig
from example_data.move_json import move_data
from example_data.module_1_json import module_1_data
from example_data.module_2_json import module_2_data
from example_data.sparring_json import sparring_data


def insert_moves():
    """Insert portion of moves data into testing database"""
    for i in range(len(move_data)):
        new_move = Moves(id=move_data[i]["id"], name=move_data[i]["name"], code=move_data[i]["code"],
                         belt_colour=move_data[i]["belt_colour"], lesson_plan=move_data[i]["lesson_plan"],
                         related_moves=move_data[i]["related_moves"], module_combo=move_data[i]["module_combo"],
                         is_defence=move_data[i]["is_defence"], is_kick=move_data[i]["is_kick"],
                         is_jump=move_data[i]["is_jump"], notes=move_data[i]["notes"])
        db.session.add(new_move)
        db.session.commit()


def insert_combo(module, data):
    for i in range(len(data)):
        new_combo = module(id=data[i]["id"], name=data[i]["name"], code=data[i]["code"], moves=data[i]["moves"],
                           is_kick=data[i]["is_kick"], is_jump=data[i]["is_jump"], notes=data[i]["notes"])
        db.session.add(new_combo)
        db.session.commit()


def insert_spar_combo():
    for i in range(len(sparring_data)):
        new_combo = SparringCombination(id=sparring_data[i]["id"], code=sparring_data[i]["code"],
                                        belt_colour=sparring_data[i]["belt_colour"], attack=sparring_data[i]["attack"],
                                        defence=sparring_data[i]["defence"], attack_id=sparring_data[i]["attack_id"],
                                        defence_id=sparring_data[i]["defence_id"], notes=sparring_data[i]["notes"])
        db.session.add(new_combo)
        db.session.commit()


class TestAPI(TestCase):
    """Base class for testing moves and combinations"""

    def setUp(self) -> None:
        """Set up test database tables and insert data"""
        self.app = create_app(TestConfig)
        self.client = self.app.test_client(self)

        with self.app.app_context():
            db.create_all()
            insert_moves()
            insert_combo(ModuleOne, module_1_data)
            insert_combo(ModuleTwo, module_2_data)
            insert_spar_combo()

    def tearDown(self) -> None:
        """Drop tables"""
        with self.app.app_context():
            db.session.remove()
            db.drop_all()


if __name__ == "__main__":
    unittest.main()
