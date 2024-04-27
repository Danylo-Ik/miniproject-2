import unittest
from solution import flatten

class TestFlatten(unittest.TestCase):

    def test_single_level(self):
        self.assertEqual(flatten([1, 2, 3]), [1, 2, 3])
    
    def test_nested_lists(self):
        self.assertEqual(flatten([1, [2, 3], [4, [5, 6]]]), [1, 2, 3, 4, 5, 6])
    
    def test_empty_lists(self):
        self.assertEqual(flatten([]), [])
    
    def test_empty_nested_lists(self):
        self.assertEqual(flatten([[], [[]], [[[]]]]), [])
    
    def test_mix_of_types(self):
        self.assertEqual(flatten([1, "string", [3.14, [True, False]]]), [1, "string", 3.14, True, False])
    
    def test_single_element(self):
        self.assertEqual(flatten([42]), [42])
    
    def test_already_flat(self):
        self.assertEqual(flatten([1, 2, 3, 4]), [1, 2, 3, 4])
    
    def test_mixed_levels(self):
        self.assertEqual(flatten([[1], 2, [[3]], 4]), [1, 2, 3, 4])
    
    def test_list_with_none(self):
        self.assertEqual(flatten([None, [1, None], [2, 3, None]]), [None, 1, None, 2, 3, None])
    
    def test_non_list_input(self):
        # Handling non-list input, expected to return the input as it is
        self.assertEqual(flatten(10), 10)
        self.assertEqual(flatten("string"), "string")

# If running as a script, execute the unittests.
if __name__ == "__main__":
    unittest.main()
