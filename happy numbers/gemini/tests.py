import unittest
from solution import sieve_flavius

class TestSieveFlavius(unittest.TestCase):
    def test_positive_values(self):
        self.assertEqual(sieve_flavius(20), [1, 3, 7, 9, 13, 15])
        self.assertEqual(sieve_flavius(100), [1, 3, 7, 9, 13, 15, 21, 25, 31, 33, 37, 43, 49, 51, 63, 67, 69, 73, 75, 79, 87, 93, 99])

    def test_zero(self):
        self.assertEqual(sieve_flavius(0), [])

    def test_negative_values(self):
        self.assertEqual(sieve_flavius(-5), None)
        self.assertEqual(sieve_flavius(-1), None)

    def test_non_numeric_input(self):
        self.assertEqual(sieve_flavius("hello"), None)

if __name__ == "__main__":
    unittest.main()
