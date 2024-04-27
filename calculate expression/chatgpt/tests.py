import unittest
from expression_calculator import calculate_expression

class TestCalculator(unittest.TestCase):

    def test_addition(self):
        self.assertEqual(calculate_expression("Скільки буде 8 додати 3?"), 11)

    def test_subtraction(self):
        self.assertEqual(calculate_expression("Скільки буде 8 відняти 3?"), 5)

    def test_multiplication(self):
        self.assertEqual(calculate_expression("Скільки буде 7 помножити на 3?"), 21)

    def test_division(self):
        self.assertEqual(calculate_expression("Скільки буде 10 поділити на 2?"), 5)

    def test_multiple_operations(self):
        self.assertEqual(calculate_expression("Скільки буде 10 помножити на 2 додати 5?"), 25)

    def test_zero_division(self):
        self.assertEqual(calculate_expression("Скільки буде 5 поділити на 0?"), 'Неправильний вираз!')

    def test_invalid_expression(self):
        self.assertEqual(calculate_expression("Скільки буде 3 в кубі?"), 'Неправильний вираз!')
        self.assertEqual(calculate_expression("Скільки сезонів в році?"), 'Неправильний вираз!')
        self.assertEqual(calculate_expression("Скільки буде 2 2 додати?"), 'Неправильний вираз!')

    def test_extra_operators(self):
        self.assertEqual(calculate_expression('Скільки буде 10 додати додати 9?'), 'Неправильний вираз!')
        self.assertEqual(calculate_expression('Скільки буде -10 поділити на помножити на 3?'), 'Неправильний вираз!')

    def test_invalid_expression_format(self):
        self.assertEqual(calculate_expression('Скільки буде 9 9?'), 'Неправильний вираз!')

    def test_trailing_operator(self):
        self.assertEqual(calculate_expression('Скільки буде 10 поділити на 2'), 'Неправильний вираз!')

if __name__ == '__main__':
    unittest.main()