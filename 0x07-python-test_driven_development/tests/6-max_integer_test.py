#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    """test cases"""

    def test_norm_0(self):
        """unordered"""
        res = max_integer([1, 3, 5, 2])
        self.assertEqual(res, 5)

    def test_norm_1(self):
        """text"""
        res = max_integer(["how", "text", "lol", "zame"])
        self.assertEqual(res, "zame")

    def test_norm_2(self):
        """ordered"""
        res = max_integer([1, 3, 5, 8])
        self.assertEqual(res, 8)

    def test_norm_3(self):
        res = max_integer([])
        self.assertEqual(res, None)

    def test_norm_4(self):
        """reverse order"""
        res = max_integer([7, 5, 3, 1])
        self.assertEqual(res, 7)

    def test_norm_5(self):
        """one"""
        res = max_integer([2])
        self.assertEqual(res, 2)

    def test_norm_6(self):
        """floats"""
        res = max_integer([1.6, 3.5, 5.7, 8.8])
        self.assertEqual(res, 8.8)

    def test_norm_7(self):
        """ordered"""
        res = max_integer([1, 3.2, 5.5, 8])
        self.assertEqual(res, 8)

    def test_norm_8(self):
        """string"""
        res = max_integer("azar")
        self.assertEqual(res, 'z')

    def test_norm_9(self):
        """emp"""
        res = max_integer("")
        self.assertEqual(res, None)


if __name__ == '__main__':
    unittest.main()
