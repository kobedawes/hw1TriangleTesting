from unittest import TestCase
import main
import math


class Test(TestCase):
    def test_classify_triangle(self):
        self.assertEqual(main.classify_triangle(5, 12, 13), print('right'))
        self.assertEqual(main.classify_triangle(1, 1, math.sqrt(2)), print('right'))
        self.assertEqual(main.classify_triangle(3, 4, 5), print('right'))
        self.assertEqual(main.classify_triangle(math.sqrt(3), 1, 2), print('right'))
        self.assertEqual(main.classify_triangle(1, 1, 3), print('isosceles'))
        self.assertEqual(main.classify_triangle(3, 1, 3), print('isosceles'))
        self.assertEqual(main.classify_triangle(5, 1, 1), print('isosceles'))
        self.assertEqual(main.classify_triangle(1, 1, 1), print('equilateral'))
        self.assertEqual(main.classify_triangle(3, 3, 3), print('equilateral'))
        self.assertEqual(main.classify_triangle(5, 5, 5), print('equilateral'))
        self.assertEqual(main.classify_triangle(1, 2, 3), print('scalene'))
        self.assertEqual(main.classify_triangle(7, 5, 12), print('scalene'))
        self.assertEqual(main.classify_triangle(5, 6, 8), print('scalene'))



