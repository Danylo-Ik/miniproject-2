import unittest
from solution import sieve_flavius

class TestSieveFlavius(unittest.TestCase):

    def test_positive_input(self):
        self.assertEqual(sieve_flavius(20), [1, 3, 7, 9, 13, 15])

    def test_positive_large_input(self):
        self.assertEqual(sieve_flavius(100), [1, 3, 7, 9, 13, 15, 21, 25, 31, 33, 37, 43, 49, 51, 63, 67, 69, 73, 75, 79, 87, 93, 99])

    def test_negative_input(self):
        self.assertIsNone(sieve_flavius(-5))

    def test_zero_input(self):
        self.assertEqual(sieve_flavius(0), [])

    def test_one_input(self):
        self.assertEqual(sieve_flavius(1), [1])

    def test_even_input(self):
        self.assertEqual(sieve_flavius(4), [1, 3])

    def test_float_input(self):
        self.assertIsNone(sieve_flavius(5.5))

    def test_string_input(self):
        self.assertIsNone(sieve_flavius("hello"))


if __name__ == "__main__":
    unittest.main()
