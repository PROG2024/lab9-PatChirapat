"""Unit tests of the Circle class using unittest or pytest (your choice).

Write unit tests as described in README.md.

1. Unit test for add_area using typical values.
2. Unit test for add_area for an "edge case" where one circle has radius 0.
3. Unit test that circle constructor raises exception of radius is negative.

"""
import unittest
from math import hypot, pi
from circle import Circle

class TestCircle(unittest.TestCase):

    def setUp(self):
        self.c1 = Circle(3) # typical value
        self.c2 = Circle(4) # typical value
        self.c3 = Circle(0) # edge case
        self.c4 = None

    def test_add_area_typical(self):
        circle = self.c1.add_area(self.c2)
        radius1 = self.c1.get_radius()
        radius2 = self.c2.get_radius()
        final_radius = hypot(radius1, radius2)
        area = pi * final_radius ** 2

        self.assertAlmostEqual(circle.get_area(), area, places=5)

    def test_add_area_edge_case(self):
        circle = self.c1.add_area(self.c3)
        radius1 = self.c1.get_radius()
        radius2 = self.c3.get_radius()
        final_radius = hypot(radius1, radius2)
        area = pi * final_radius ** 2

        self.assertAlmostEqual(circle.get_area(), area, places=5)

    def test_negative_radius(self):
        with self.assertRaises(ValueError):
            self.c4 = Circle(-1)

