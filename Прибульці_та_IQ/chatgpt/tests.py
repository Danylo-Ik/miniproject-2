import unittest

from solution import read_file, rescue_people

class TestAliensIQ(unittest.TestCase):

    def test_read_file(self):
        # Test empty file
        with open('empty_file.txt', 'w') as file:
            file.write('')
        self.assertEqual(read_file('empty_file.txt'), {})

        # Test file with valid data
        with open('test_file.txt', 'w') as file:
            file.write('Steve Jobs,160\nAlbert Einstein,160\nSir Isaac Newton,195\nNikola Tesla,189\n')
        expected_output = {"Steve Jobs": 160, "Albert Einstein": 160, "Sir Isaac Newton": 195, "Nikola Tesla": 189}
        self.assertEqual(read_file('test_file.txt'), expected_output)

    def test_rescue_people(self):
        # Test empty list
        self.assertEqual(rescue_people({}, 500), (0, []))

        # Test when all IQs are below the limit
        smarties = {"John Doe": 100, "Jane Doe": 120}
        self.assertEqual(rescue_people(smarties, 500), (0, []))

        # Test when all IQs are above the limit
        smarties = {"Steve Jobs": 160, "Albert Einstein": 160, "Sir Isaac Newton": 195, "Nikola Tesla": 189}
        self.assertEqual(rescue_people(smarties, 150), (0, []))

        # Test with mixed IQs
        smarties = {"Steve Jobs": 160, "Albert Einstein": 160, "Sir Isaac Newton": 195, "Nikola Tesla": 189}
        self.assertEqual(rescue_people(smarties, 500), (2, [['Sir Isaac Newton', 'Nikola Tesla'], ['Albert Einstein', 'Steve Jobs']]))

        # Test with single person whose IQ exceeds the limit
        smarties = {"Sir Isaac Newton": 195}
        self.assertEqual(rescue_people(smarties, 100), (0, []))

if __name__ == '__main__':
    unittest.main()
