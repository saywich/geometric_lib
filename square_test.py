import unittest
from square import area, perimeter


class SquareTestCase(unittest.TestCase):
    def test_area(self):
        result = area(10)
        self.assertEqual(result, 100)

    def test_perimeter(self):
        result = perimeter(10)
        self.assertEqual(result, 40)
