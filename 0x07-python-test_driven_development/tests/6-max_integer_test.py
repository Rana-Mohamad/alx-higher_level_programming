#!/usr/bin/python3
'''Unittest for max_integer([..])'''

import unittest
max_integer = __import__("6-max_integer").max_integer

class TestMaxInteger(unittest.TestCase):
    def test_no_arg(self):
        self.assertEqual(max_integer(), None)

    def test_empty_list(self):
        self.assertEqual(max_integer([]), None)

    def test_single(self):
        self.assertEqual(max_integer([5]), 5)

    def test_identical(self):
        self.assertEqual(max_integer([3, 3, 3]), 3)

    def test_max(self):
        self.assertEqual(max_integer([2, 5, 8, 3, 9, 1]), 9)

    def test_negative_positive(self):
        self.assertEqual(max_integer([5, -9, 98, -399, 200]), 200)

    def test_negative(self):
        self.assertEqual(max_integer([-1, -36, -555, -986554, -98]), -1)

    def test_int_float(self):
        self.assertEqual(max_integer([2.5, 100, 78.25, 999.99, 35]), 999.99)

    def test_float(self):
        self.assertEqual(max_integer([5.5, 8.25, 30.2, 50.25, 70.6, 99.5, 0.538]), 99.5)


if __name__ == "__main__":
    unittest.main()
