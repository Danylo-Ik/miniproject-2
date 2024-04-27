import unittest
from solution import flatten


class TestFlatten(unittest.TestCase):

    def test_empty_list(self):
        """Test flattening an empty list."""
        self.assertEqual(flatten([]), [])

    def test_single_element_list(self):
        """Test flattening a list with a single element."""
        self.assertEqual(flatten([1]), [1])

    def test_single_nested_list(self):
        """Test flattening a list with a single nested list."""
        self.assertEqual(flatten([[[1, 2]]]), [1, 2])

    def test_multiple_nested_lists(self):
        """Test flattening a list with multiple nested lists."""
        self.assertEqual(flatten([[1, 2], [3, 4], [5]]), [1, 2, 3, 4, 5])

    def test_mixed_list(self):
        """Test flattening a list with mixed types."""
        self.assertEqual(flatten([1, [2, 3], "string"]), [1, 2, 3, "string"])

    def test_empty_nested_list(self):
        """Test flattening a list with an empty nested list."""
        self.assertEqual(flatten([[1], [], [3]]), [1, 3])

    def test_non_list_input(self):
        """Test flattening a non-list input."""
        self.assertEqual(flatten(10), 10)
        self.assertEqual(flatten("string"), "string")


if __name__ == "__main__":
  unittest.main()