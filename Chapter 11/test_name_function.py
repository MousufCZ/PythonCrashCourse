import unittest
from name_function import get_formatted_name

class NameTestCase(unittest.TestCase):
    """Tests for this whole module"""

    def test_first_name(self):
        """DOes the name work when importing the function:: get_formatted_name"""
        formatted_name = get_formatted_name('Mousuf','chow')
        self.assertEqual(formatted_name, 'Mousuf Chow')

unittest.main()
