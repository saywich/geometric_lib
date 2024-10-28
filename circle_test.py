import unittest
from circle import area, perimeter

from math import pi


class CircleTestCase(unittest.TestCase):
    def test_area(self):
        r = 10
        result = area(r)
        self.assertEqual(result, pi * (r ** 2))

    def test_perimeter(self):
        r = 10
        result = perimeter(r)
        self.assertEqual(result, 2 * pi * r)
