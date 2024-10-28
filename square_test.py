import unittest
from square import area, perimeter


class SquareTestCase(unittest.TestCase):
    # Area
    def test_area(self):
        result = area(10)
        self.assertEqual(result, 100)
    
    def test_string_area(self):
        result = area("10")
        self.assertEqual(result, 100)

    def test_zero_area(self):
        self.assertRaises(ValueError, area, 0)

    def test_negative_area(self):
        self.assertRaises(ValueError, area, -10)

    # Perimeter
    def test_perimeter(self):
        result = perimeter(10)
        self.assertEqual(result, 40)
    
    def test_string_perimeter(self):
        result = perimeter("10")
        self.assertEqual(result, 40)

    def test_zero_perimeter(self):
        self.assertRaises(ValueError, perimeter, 0)

    def test_negative_perimeter(self):
        self.assertRaises(ValueError, perimeter, -10)
