import unittest
from circle import area, perimeter

from math import pi


class CircleTestCase(unittest.TestCase):
    # Area
    def test_area(self):
        r = 10
        result = area(r)
        self.assertEqual(result, pi * (r ** 2))
    
    def test_string_area(self):
        r = "10"
        result = area(r)
        self.assertEqual(result, pi * int(r) ** 2)

    def test_zero_area(self):
        self.assertRaises(ValueError, area, 0)

    def test_negative_area(self):
        self.assertRaises(ValueError, area, -10)

    # Perimeter
    def test_perimeter(self):
        r = 10
        result = perimeter(r)
        self.assertEqual(result, 2 * pi * r)
    
    def test_string_perimeter(self):
        r = "10"
        result = perimeter(r)
        self.assertEqual(result, 2 * pi * int(r))

    def test_zero_perimeter(self):
        self.assertRaises(ValueError, perimeter, 0)

    def test_negative_perimeter(self):
        self.assertRaises(ValueError, perimeter, -10)
