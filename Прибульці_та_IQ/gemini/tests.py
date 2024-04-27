import unittest
from solution import rescue_people, read_file

class TestAlienRescue(unittest.TestCase):

    def test_empty_file(self):
        """Test with an empty file."""
        data = {}
        rides, evacuees = rescue_people(data, 100)
        self.assertEqual(rides, 0)
        self.assertEqual(evacuees, [])

    def test_no_high_iq(self):
        """Test with everyone having IQ below 130."""
        data = {"John": 120, "Jane": 115}
        rides, evacuees = rescue_people(data, 100)
        self.assertEqual(rides, 0)
        self.assertEqual(evacuees, [])

    def test_single_person(self):
        """Test with a single person with high IQ."""
        data = {"Einstein": 160}
        rides, evacuees = rescue_people(data, 100)
        self.assertEqual(rides, 1)
        self.assertEqual(evacuees, [["Einstein"]])

    def test_multiple_people_one_ride(self):
        """Test with multiple people fitting on one ride."""
        data = {"Einstein": 140, "Jobs": 135}
        rides, evacuees = rescue_people(data, 275)
        self.assertEqual(rides, 1)
        self.assertEqual(evacuees, [["Einstein", "Jobs"]])

    def test_person_with_iq_equal_to_limit(self):
        """Test with a person with IQ equal to the limit."""
        data = {"Newton": 150}
        rides, evacuees = rescue_people(data, 150)
        self.assertEqual(rides, 1)
        self.assertEqual(evacuees, [["Newton"]])

if __name__ == '__main__':
    unittest.main()
