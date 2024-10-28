import unittest
from triangle import area, perimeter


class TriangleTestCase(unittest.TestCase):
    def test_area(self):
        result = area(10, 10)
        self.assertEqual(result, 50)

    def test_perimeter(self):
        result = perimeter(10, 10, 10)
        self.assertEqual(result, 30)
