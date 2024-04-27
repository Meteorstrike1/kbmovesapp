import unittest
from test_class import TestAPI

endpoint = "/sparring"


class TestSparring(TestAPI):
    """Testing Sparring Combinations table"""

    def test_get_all_combinations(self):
        """Get all combinations"""
        get_response = self.client.get(f"{endpoint}/all")
        status_code = get_response.status_code
        expected = 4
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
        id = 27
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

    def test_get_attack_in_combination_by_id_success(self):
        """Get attack move in sparring combination by id, found"""
        id = 1
        get_response = self.client.get(f"{endpoint}/attack_move/{id}")
        status_code = get_response.status_code
        expected = "snap punch"
        result = get_response.json["name"]

        self.assertEqual(status_code, 200)
        self.assertEqual(expected, result)

    def test_get_attack_in_combination_by_id_not_found_fail(self):
        """Get attack move in sparring combination by id, not found"""
        id = 27
        get_response = self.client.get(f"{endpoint}/attack_move/{id}")
        status_code = get_response.status_code

        self.assertEqual(status_code, 404)

    def test_get_attack_in_combination_by_id_move_missing_fail(self):
        """Get attack move in sparring combination by id that doesn't exist in data"""
        id = 3
        get_response = self.client.get(f"{endpoint}/combo_moves/{id}")
        status_code = get_response.status_code

        self.assertEqual(status_code, 404)

    def test_get_attack_in_combination_by_id_none_fail(self):
        """Get attack move in sparring combination by id, no move to search"""
        id = 99
        get_response = self.client.get(f"{endpoint}/combo_moves/{id}")
        status_code = get_response.status_code

        self.assertEqual(status_code, 404)

    def test_get_defences_in_combination_by_id_success(self):
        """Get list of defence moves in sparring combination by id, found"""
        id = 1
        get_response = self.client.get(f"{endpoint}/defence_moves/{id}")
        status_code = get_response.status_code
        expected = "palm deflection front arm"
        result = get_response.json[2]["name"]

        self.assertEqual(status_code, 200)
        self.assertEqual(expected, result)

    def test_get_defences_in_combination_by_id_not_found_fail(self):
        """Get list of defence moves in sparring combination by id, not found"""
        id = 27
        get_response = self.client.get(f"{endpoint}/defence_moves/{id}")
        status_code = get_response.status_code

        self.assertEqual(status_code, 404)

    def test_get_defences_in_combination_by_id_missing_fail(self):
        """Get list of defence moves in sparring combination by id that doesn't exist in the Move table data"""
        id = 3
        get_response = self.client.get(f"{endpoint}/defence_moves/{id}")
        status_code = get_response.status_code

        self.assertEqual(status_code, 404)

    def test_get_defences_in_combination_by_id_none_fail(self):
        """Get list of defence moves in sparring combination by id, no move to search"""
        id = 99
        get_response = self.client.get(f"{endpoint}/defence_moves/{id}")
        status_code = get_response.status_code
        expected = {'message': f'No combination moves. You have requested this URI [/sparring/defence_moves/{id}] '
                               f'but did you mean /sparring/defence_moves/<int:id> or /sparring/attack_move/<int:id> '
                               f'or /sparring/id/<int:id> ?'}
        result = get_response.json

        self.assertEqual(status_code, 404)
        self.assertEqual(expected, result)


if __name__ == "__main__":
    unittest.main()
