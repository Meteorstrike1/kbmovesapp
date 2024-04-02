import unittest
from app import create_app, db
from models import Moves
from test_class import TestAPI

endpoint = "/moves"


class TestMoves(TestAPI):
    """Testing Moves table"""

    def test_get_all_moves(self):
        """Get all moves"""
        get_response = self.client.get(f"{endpoint}/all")
        status_code = get_response.status_code
        expected = 24
        result = len(get_response.json)

        self.assertEqual(status_code, 200)
        self.assertEqual(expected, result)

    def test_get_move_by_id_success(self):
        """Move by id, found"""
        id = 1
        get_response = self.client.get(f"{endpoint}/id/{id}")
        status_code = get_response.status_code

        self.assertEqual(status_code, 200)

    def test_get_move_by_id_fail(self):
        """Move by id, not found"""
        id = 211
        get_response = self.client.get(f"{endpoint}/id/{id}")
        status_code = get_response.status_code

        self.assertEqual(status_code, 404)

    def test_get_move_by_id_fail_invalid(self):
        """Move by id, invalid input"""
        id = "test"
        get_response = self.client.get(f"{endpoint}/id/{id}")
        status_code = get_response.status_code

        self.assertEqual(status_code, 404)

    def test_get_move_by_code_success(self):
        """Move by code, found"""
        code = "RW1"
        get_response = self.client.get(f"{endpoint}/code/{code}")
        status_code = get_response.status_code

        self.assertEqual(status_code, 200)

    def test_get_move_by_code_fail(self):
        """Move by code, not found"""
        code = "T1"
        get_response = self.client.get(f"{endpoint}/code/{code}")
        status_code = get_response.status_code

        self.assertEqual(status_code, 404)

    def test_get_moves_by_belt_success(self):
        """List of moves by belt, found"""
        belt = "red white"
        get_response = self.client.get(f"{endpoint}/belt/{belt}")
        status_code = get_response.status_code
        expected = 12
        result = len(get_response.json)

        self.assertEqual(status_code, 200)
        self.assertEqual(expected, result)

    def test_get_moves_by_belt_fail(self):
        """List of moves by belt, not found"""
        belt = "testing"
        get_response = self.client.get(f"{endpoint}/belt/{belt}")
        status_code = get_response.status_code

        self.assertEqual(status_code, 404)

    def test_get_moves_by_name_exact_success(self):
        """List of moves by full name search, found"""
        name = "roundhouse kick back leg land forward"
        get_response = self.client.get(f"{endpoint}/name/{name}")
        status_code = get_response.status_code
        expected = 1
        result = len(get_response.json)

        self.assertEqual(status_code, 200)
        self.assertEqual(expected, result)

    def test_get_moves_by_name_exact_mixed_case_success(self):
        """List of moves by full name search, mixed case, found"""
        name = "RIDGehand stRIke to groin FRONT ARM"
        get_response = self.client.get(f"{endpoint}/name/{name}")
        status_code = get_response.status_code
        expected = 1
        result = len(get_response.json)

        self.assertEqual(status_code, 200)
        self.assertEqual(expected, result)

    def test_get_moves_by_name_partial_success(self):
        """List of moves by partial name search, found"""
        name = "backfist"
        get_response = self.client.get(f"{endpoint}/name/{name}")
        status_code = get_response.status_code
        expected = 3
        result = len(get_response.json)

        self.assertEqual(status_code, 200)
        self.assertEqual(expected, result)

    def test_get_moves_by_name_fail(self):
        """List of moves by name search, not found"""
        name = "testing kick strike"
        get_response = self.client.get(f"{endpoint}/name/{name}")
        status_code = get_response.status_code

        self.assertEqual(status_code, 404)

    def test_get_moves_by_name_out_of_order_fail(self):
        """List of moves by name search, move exists but words out of order"""
        name = "backfist turning"
        get_response = self.client.get(f"{endpoint}/name/{name}")
        status_code = get_response.status_code

        self.assertEqual(status_code, 404)

    def test_get_graded_hand_defences_success(self):
        """List of hand defences tested at purple and brown white belt, found"""
        get_response = self.client.get(f"{endpoint}/hand_defences/graded")
        status_code = get_response.status_code
        expected = 4
        result = len(get_response.json)

        self.assertEqual(status_code, 200)
        self.assertEqual(expected, result)

    def test_get_all_hand_defences_success(self):
        """List of all hand defences (same as previous result because no test data above BrW belt), found"""
        get_response = self.client.get(f"{endpoint}/hand_defences/all")
        status_code = get_response.status_code
        expected = 4
        result = len(get_response.json)

        self.assertEqual(status_code, 200)
        self.assertEqual(expected, result)

    def test_get_all_leg_defences_success(self):
        """List of all leg defences, found"""
        get_response = self.client.get(f"{endpoint}/leg_defences/all")
        status_code = get_response.status_code
        expected = 2
        result = len(get_response.json)

        self.assertEqual(status_code, 200)
        self.assertEqual(expected, result)

    def test_get_all_moves_in_module_one_success(self):
        """List of all moves that appear in module 1"""
        get_response = self.client.get(f"{endpoint}/in_module_1")
        status_code = get_response.status_code
        expected = 11
        result = len(get_response.json)

        self.assertEqual(status_code, 200)
        self.assertEqual(expected, result)

    def test_get_all_moves_in_module_two_success(self):
        """List of all moves that appear in module 2"""
        get_response = self.client.get(f"{endpoint}/in_module_2")
        status_code = get_response.status_code
        expected = 8
        result = len(get_response.json)

        self.assertEqual(status_code, 200)
        self.assertEqual(expected, result)

    def test_get_all_moves_not_in_module_one_success(self):
        """List of all moves that don't appear in module 1"""
        get_response = self.client.get(f"{endpoint}/not_module_1")
        status_code = get_response.status_code
        expected = 1
        result = len(get_response.json)

        self.assertEqual(status_code, 200)
        self.assertEqual(expected, result)

    def test_get_all_moves_not_in_module_two_success(self):
        """List of all moves that don't appear in module 2"""
        get_response = self.client.get(f"{endpoint}/not_module_2")
        status_code = get_response.status_code
        expected = 4
        result = len(get_response.json)

        self.assertEqual(status_code, 200)
        self.assertEqual(expected, result)

    def test_get_all_moves_not_jump_or_kick_success(self):
        """List of all moves that don't involve jump or kick"""
        get_response = self.client.get(f"{endpoint}/not_jump_or_kick")
        status_code = get_response.status_code
        expected = 16
        result = len(get_response.json)

        self.assertEqual(status_code, 200)
        self.assertEqual(expected, result)

    def test_get_all_moves_not_jump_success(self):
        """List of all moves that don't involve jump"""
        get_response = self.client.get(f"{endpoint}/not_jump")
        status_code = get_response.status_code
        expected = 23
        result = len(get_response.json)

        self.assertEqual(status_code, 200)
        self.assertEqual(expected, result)

    def test_get_all_moves_not_kick_success(self):
        """List of all moves that don't involve kick"""
        get_response = self.client.get(f"{endpoint}/not_kick")
        status_code = get_response.status_code
        expected = 16
        result = len(get_response.json)

        self.assertEqual(status_code, 200)
        self.assertEqual(expected, result)

    def test_get_all_moves_with_kick_success(self):
        """List of all moves that involve kick"""
        get_response = self.client.get(f"{endpoint}/is_kick")
        status_code = get_response.status_code
        expected = 8
        result = len(get_response.json)

        self.assertEqual(status_code, 200)
        self.assertEqual(expected, result)

    def test_get_all_moves_with_jump_success(self):
        """List of all moves that involve jump"""
        get_response = self.client.get(f"{endpoint}/is_jump")
        status_code = get_response.status_code
        expected = 1
        result = len(get_response.json)

        self.assertEqual(status_code, 200)
        self.assertEqual(expected, result)

    def test_get_all_moves_with_jump_kick_success(self):
        """List of all moves that involve jump kick"""
        get_response = self.client.get(f"{endpoint}/is_jump_kick")
        status_code = get_response.status_code
        expected = 1
        result = len(get_response.json)
        print(result)

        self.assertEqual(status_code, 200)
        self.assertEqual(expected, result)


if __name__ == "__main__":
    unittest.main()
