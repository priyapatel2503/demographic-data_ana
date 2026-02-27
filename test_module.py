import unittest
from demographic_data_analyzer import calculate_demographic_data


class DemographicAnalyzerTestCase(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.data = calculate_demographic_data()

    def test_race_count(self):
        self.assertEqual(self.data['race_count']['White'], 27816)


if __name__ == "__main__":
    unittest.main()