import unittest

from main import max_subarray


class Test(unittest.TestCase):

    def test_ordinary_case(self):
        test_array = [-2, -3, 4, -1, 2, 5, -3]
        self.assertEqual(max_subarray(test_array), [4, -1, 2, 5])

    def test_stress_case(self):
        test_array = [-1, 3, 1, 6, -2, -12, 10, -14, 2, 2, 2, 2, 2, -20, 3, 1, 2, 2, 2, -20, 1]
        self.assertEqual(max_subarray(test_array), [2, 2, 2, 2, 2])

    #  задача имеет смысл, если в исходной последовательности будут встречаться,
    #  как положительные, так и отрицательные элементы
    def test_negative_case(self):
        test_array = [-5, -2, -3, -4, -1]
        self.assertEqual(max_subarray(test_array), [])

    def test_empty_case(self):
        test_array = []
        self.assertEqual(max_subarray(test_array), [])

    def test_positive_case(self):
        test_array = [1, 2, 3, 4, 5]
        self.assertEqual(max_subarray(test_array), [1, 2, 3, 4, 5])
