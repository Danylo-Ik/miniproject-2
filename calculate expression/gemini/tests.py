import unittest
from expression_calculator import calculate_expression
class TestCalculateExpression(unittest.TestCase):

    def test_simple_addition(self):
        self.assertEqual(calculate_expression("Скільки буде 2 додати 3?"), 5)

    def test_simple_subtraction(self):
        self.assertEqual(calculate_expression("Скільки буде 5 відняти 2?"), 3)

    def test_simple_multiplication(self):
        self.assertEqual(calculate_expression("Скільки буде 4 помножити на 3?"), 12)

    def test_simple_division(self):
        self.assertEqual(calculate_expression("Скільки буде 10 поділити на 2?"), 5)

    def test_chained_operations(self):
        self.assertEqual(calculate_expression("Скільки буде 2 додати 3 помножити на 4?"), 14)
        self.assertEqual(calculate_expression("Скільки буде 10 поділити на 2 додати 5?"), 7)
        self.assertEqual(calculate_expression("Скільки буде 4 помножити на 3 відняти 2?"), 10)

    def test_invalid_expression(self):
        self.assertEqual(calculate_expression("Скільки буде 2 3 +?"), "Неправильний вираз!")
        self.assertEqual(calculate_expression("Скільки буде 2 * 3 / 0?"), "Неправильний вираз!")
        self.assertEqual(calculate_expression("Скільки буде 2 + 3 * -4?"), -5)

if __name__ == '__main__':
    unittest.main()
