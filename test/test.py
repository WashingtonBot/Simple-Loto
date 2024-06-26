"""Module providing a class of functions testing loto.py"""

import unittest
import sys
sys.path.append(
    "C:\\Users\\azert\\Desktop\\Programme\\Nouveau dossier\\Simple-Loto\\src")
from loto import compute_gains


class TestString(unittest.TestCase):
    """Class for all the tests"""
    def test_should_return_list(self):
        """
        Testing functions from loto.py
        """
        loto_grids_combined = [2, 5, 8]
        min_value = 1
        grid_length = 6
        expected_value = 25
        self.assertEqual(compute_gains(loto_grids_combined, min_value, grid_length), expected_value)

    def test_should_return_list_2(self):
        """
        Testing functions from loto.py
        """
        loto_grids_combined = [2, 5, 8]
        min_value = 1
        grid_length = 6
        expected_value = 25
        self.assertEqual(compute_gains(loto_grids_combined, min_value, grid_length), expected_value)


if __name__ == "__main__":
    unittest.main()
