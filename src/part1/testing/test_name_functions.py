import unittest
from name_functions import get_formatted_name


class NamesTestCase(unittest.TestCase):
    """Tests for 'name_function.py'."""

    def test_first_last_name(self):
        """Do names like 'Aretha Franklin' work?"""
        formatted_name = get_formatted_name("aretha", "franklin")
        self.assertEqual(formatted_name, "Aretha Franklin")

    def test_first_last_middle_name(self):
        """Do names like 'Wolfgang Amadeus Mozart' work?"""
        formatted_name = get_formatted_name("wolfgang", "mozart", "amadeus")
        self.assertEqual(formatted_name, "Wolfgang Amadeus Mozart")

if __name__ == '__main__':
    unittest.main()
