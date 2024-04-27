import unittest
from test_class import TestAPI

endpoint = "module_1"


class TestModuleOne(TestAPI):
    """Testing Module 1 table"""
    def test_get_all_combinations(self):
        """Get all combinations"""
        get_response = self.client.get(f"{endpoint}/all")
        status_code = get_response.status_code
        expected = 7
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
        id = 26
        get_response = self.client.get(f"{endpoint}/id/{id}")
        status_code = get_response.status_code

        self.assertEqual(status_code, 404)

    def test_get_combination_by_code_success(self):
        """Combination by code, found"""
        code = "M1_3"
        get_response = self.client.get(f"{endpoint}/code/{code}")
        status_code = get_response.status_code

        self.assertEqual(status_code, 200)

    def test_get_combination_by_code_fail(self):
        """Combination by code, not found"""
        code = "T1"
        get_response = self.client.get(f"{endpoint}/code/{code}")
        status_code = get_response.status_code

        self.assertEqual(status_code, 404)

    def test_get_moves_in_combination_by_id_success(self):
        """List of moves in combination by id, found"""
        id = 1
        get_response = self.client.get(f"{endpoint}/combo_moves/{id}")
        status_code = get_response.status_code
        expected = "snap punch"
        result = get_response.json[0]["name"]

        self.assertEqual(status_code, 200)
        self.assertEqual(expected, result)

    def test_get_moves_in_combination_by_id_none_fail(self):
        """List of moves in combination by id, no move to search"""
        id = 99
        get_response = self.client.get(f"{endpoint}/combo_moves/{id}")
        status_code = get_response.status_code
        expected = {'message': f'No combination moves. You have requested this URI [/module_1/combo_moves/{id}] '
                               f'but did you mean /module_1/combo_moves/<string:code> '
                               f'or /module_2/combo_moves/<string:code> or /module_1/code/<string:code> ?'}
        result = get_response.json

        self.assertEqual(status_code, 404)
        self.assertEqual(expected, result)

    def test_get_moves_in_combination_by_id_not_found(self):
        """List of moves in combination by id, not found"""
        id = 26
        get_response = self.client.get(f"{endpoint}/combo_moves/{id}")
        status_code = get_response.status_code

        self.assertEqual(status_code, 404)

    def test_get_combination_by_id_move_missing_fail(self):
        """List of moves in combination by id that doesn't exist in the Move table data"""
        id = 4
        get_response = self.client.get(f"{endpoint}/combo_moves/{id}")
        status_code = get_response.status_code
        expected = {'message': f'Combination moves could not be found. You have requested this URI '
                               f'[/module_1/combo_moves/{id}] but did you mean /module_1/combo_moves/<string:code> '
                               f'or /module_2/combo_moves/<string:code> or /module_1/code/<string:code> ?'}
        result = get_response.json

        self.assertEqual(status_code, 404)
        self.assertEqual(expected, result)

    def test_get_moves_in_combination_by_code_success(self):
        """List of moves in combination by code, found"""
        code = "M1_1"
        get_response = self.client.get(f"{endpoint}/combo_moves/{code}")
        status_code = get_response.status_code
        expected = "snap punch"
        result = get_response.json[0]["name"]

        self.assertEqual(status_code, 200)
        self.assertEqual(expected, result)

    def test_get_combination_by_code_none_fail(self):
        """List of moves in combination by id, not found"""
        code = "M1_99"
        get_response = self.client.get(f"{endpoint}/combo_moves/{code}")
        status_code = get_response.status_code
        expected = {'message': f'No combination moves. You have requested this URI [/module_1/combo_moves/{code}] '
                               f'but did you mean /module_1/combo_moves/<string:code> '
                               f'or /module_2/combo_moves/<string:code> or /module_1/code/<string:code> ?'}
        result = get_response.json

        self.assertEqual(status_code, 404)
        self.assertEqual(expected, result)

    def test_get_combination_by_missing_code_fail(self):
        """List of moves in combination by code that doesn't exist in the Move table data"""
        code = "M1_26"
        get_response = self.client.get(f"{endpoint}/combo_moves/{code}")
        status_code = get_response.status_code

        self.assertEqual(status_code, 404)

    def test_get_combination_by_code_missing_fail(self):
        """List of moves in combination by code, not found"""
        code = "M1_4"
        get_response = self.client.get(f"{endpoint}/combo_moves/{code}")
        status_code = get_response.status_code
        expected = {'message': f'Combination moves could not be found. You have requested this URI '
                               f'[/module_1/combo_moves/{code}] but did you mean /module_1/combo_moves/<string:code> '
                               f'or /module_2/combo_moves/<string:code> or /module_1/code/<string:code> ?'}
        result = get_response.json

        self.assertEqual(status_code, 404)
        self.assertEqual(expected, result)

    def test_get_all_combinations_not_jump_or_kick_success(self):
        """List of all combinations that don't involve jump or kick"""
        get_response = self.client.get(f"{endpoint}/not_jump_or_kick")
        status_code = get_response.status_code
        expected = 2
        result = len(get_response.json)

        self.assertEqual(status_code, 200)
        self.assertEqual(expected, result)

    def test_get_all_moves_not_jump_success(self):
        """List of all combinations that don't involve jump"""
        get_response = self.client.get(f"{endpoint}/not_jump")
        status_code = get_response.status_code
        expected = 6
        result = len(get_response.json)

        self.assertEqual(status_code, 200)
        self.assertEqual(expected, result)

    def test_get_all_moves_not_kick_success(self):
        """List of all combinations that don't involve kick"""
        get_response = self.client.get(f"{endpoint}/not_kick")
        status_code = get_response.status_code
        expected = 2
        result = len(get_response.json)

        self.assertEqual(status_code, 200)
        self.assertEqual(expected, result)

    def test_get_all_moves_with_kick_success(self):
        """List of all combinations that involve kick"""
        get_response = self.client.get(f"{endpoint}/is_kick")
        status_code = get_response.status_code
        expected = 5
        result = len(get_response.json)

        self.assertEqual(status_code, 200)
        self.assertEqual(expected, result)

    def test_get_all_moves_with_jump_success(self):
        """List of all combinations that involve jump"""
        get_response = self.client.get(f"{endpoint}/is_jump")
        status_code = get_response.status_code
        expected = 1
        result = len(get_response.json)

        self.assertEqual(status_code, 200)
        self.assertEqual(expected, result)

    def test_get_all_moves_with_jump_kick_success(self):
        """List of all combinations that involve jump kick"""
        get_response = self.client.get(f"{endpoint}/is_jump_kick")
        status_code = get_response.status_code
        expected = 1
        result = len(get_response.json)

        self.assertEqual(status_code, 200)
        self.assertEqual(expected, result)


if __name__ == "__main__":
    unittest.main()
