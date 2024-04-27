import unittest
from test_class import TestAPI

endpoint = "/colour"


class TestColour(TestAPI):
    """Testing Colour Combinations table"""

    def test_get_all_combinations(self):
        """Get all combinations"""
        get_response = self.client.get(f"{endpoint}/all")
        status_code = get_response.status_code
        expected = 5
        result = len(get_response.json)

        self.assertEqual(status_code, 200)
        self.assertEqual(expected, result)

    def test_get_combination_by_id_success(self):
        """Combination by id, found"""
        id = 2
        get_response = self.client.get(f"{endpoint}/id/{id}")
        status_code = get_response.status_code

        self.assertEqual(status_code, 200)

    def test_get_combination_by_id_fail(self):
        """Combination by id, not found"""
        id = 115
        get_response = self.client.get(f"{endpoint}/id/{id}")
        status_code = get_response.status_code

        self.assertEqual(status_code, 404)

    def test_get_combination_by_belt_success(self):
        """List of combinations by belt, found"""
        belt = "red white"
        get_response = self.client.get(f"{endpoint}/belt/{belt}")
        status_code = get_response.status_code
        expected = 2
        result = len(get_response.json)

        self.assertEqual(status_code, 200)
        self.assertEqual(expected, result)

    def test_get_combination_by_belt_fail(self):
        """List of combinations by belt, not found"""
        belt = "testing"
        get_response = self.client.get(f"{endpoint}/belt/{belt}")
        status_code = get_response.status_code

        self.assertEqual(status_code, 404)

    def test_get_moves_in_combination_by_id_success(self):
        """Get list of moves in colour combination by id, found"""
        id = 1
        get_response = self.client.get(f"{endpoint}/combo_moves/{id}")
        status_code = get_response.status_code
        expected = "snap punch"
        result = get_response.json[0]["name"]

        self.assertEqual(status_code, 200)
        self.assertEqual(expected, result)

    def test_get_moves_in_combination_by_id_not_found_fail(self):
        """Get list of moves in colour combination by id, not found"""
        id = 115
        get_response = self.client.get(f"{endpoint}/combo_moves/{id}")
        status_code = get_response.status_code

        self.assertEqual(status_code, 404)

    def test_get_moves_in_combination_by_id_missing_fail(self):
        """Get list of moves in colour combination by id that doesn't exist in the Move table data"""
        id = 11
        get_response = self.client.get(f"{endpoint}/combo_moves/{id}")
        status_code = get_response.status_code

        self.assertEqual(status_code, 404)

    def test_get_moves_in_combination_by_id_none_fail(self):
        """Get list of moves in colour combination by id, no move to search"""
        id = 199
        get_response = self.client.get(f"{endpoint}/combo_moves/{id}")
        status_code = get_response.status_code
        expected = {'message': f'No combination moves. You have requested this URI [/colour/combo_moves/{id}] but did '
                               f'you mean /colour/combo_moves/<int:id> or /module_2/combo_moves/<string:code> or '
                               f'/module_1/combo_moves/<string:code> ?'}
        result = get_response.json

        self.assertEqual(status_code, 404)
        self.assertEqual(expected, result)

    def test_get_all_grading_combinations_success(self):
        """List of all grading combinations"""
        get_response = self.client.get(f"{endpoint}/is_grading")
        status_code = get_response.status_code
        expected = 1
        result = len(get_response.json)

        self.assertEqual(status_code, 200)
        self.assertEqual(expected, result)

    def test_get_all_not_grading_combinations_success(self):
        """List of all non grading combinations"""
        get_response = self.client.get(f"{endpoint}/not_grading")
        status_code = get_response.status_code
        expected = 4
        result = len(get_response.json)

        self.assertEqual(status_code, 200)
        self.assertEqual(expected, result)


if __name__ == "__main__":
    unittest.main()
