import unittest
from rectangle import area, perimeter


class RectangleTestCase(unittest.TestCase):
    def test_area(self):
        result = area(10, 10)
        self.assertEqual(result, 100)

    def test_perimeter(self):
        result = perimeter(10, 10)
        self.assertEqual(result, 40)
