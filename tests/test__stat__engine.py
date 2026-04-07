import unittest
from src.stat_engine import StatEngine


class TestStatEngine(unittest.TestCase):

    def test_mean(self):
        engine = StatEngine([1, 2, 3, 4])
        self.assertEqual(engine.get_mean(), 2.5)

    def test_median_even(self):
        engine = StatEngine([1, 2, 3, 4])
        self.assertEqual(engine.get_median(), 2.5)

    def test_median_odd(self):
        engine = StatEngine([1, 2, 3])
        self.assertEqual(engine.get_median(), 2)

    def test_mode_multimodal(self):
        engine = StatEngine([1, 1, 2, 2, 3])
        self.assertCountEqual(engine.get_mode(), [1, 2])

    def test_no_mode(self):
        engine = StatEngine([1, 2, 3])
        self.assertEqual(engine.get_mode(), "No mode (all values are unique)")

    def test_empty_input(self):
        with self.assertRaises(ValueError):
            StatEngine([])

    def test_std_known_value(self):
        engine = StatEngine([2, 4, 4, 4, 5, 5, 7, 9])
        self.assertAlmostEqual(engine.get_standard_deviation(is_sample=False), 2.0)

    def test_outliers(self):
        engine = StatEngine([10, 12, 14, 100])
        outliers = engine.get_outliers()
        self.assertIn(100, outliers)


if __name__ == "__main__":
    unittest.main()
