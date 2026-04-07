import unittest
from src.stat_engine import StatEngine


class TestStatEngine(unittest.TestCase):

    def test_mean(self):
        engine = StatEngine([1, 2, 3, 4])
        self.assertEqual(engine.get_mean(), 2.5)

    def test_median_odd(self):
        engine = StatEngine([3, 1, 2])
        self.assertEqual(engine.get_median(), 2)

    def test_median_even(self):
        engine = StatEngine([1, 2, 3, 4])
        self.assertEqual(engine.get_median(), 2.5)

    def test_mode_multimodal(self):
        engine = StatEngine([1, 1, 2, 2, 3])
        self.assertEqual(set(engine.get_mode()), {1, 2})

    def test_mode_no_mode(self):
        engine = StatEngine([1, 2, 3])
        self.assertEqual(engine.get_mode(), "No mode (all values are unique)")

    def test_variance_population(self):
        engine = StatEngine([1, 2, 3])
        self.assertAlmostEqual(engine.get_variance(is_sample=False), 2/3)

    def test_std_population(self):
        engine = StatEngine([1, 2, 3])
        self.assertAlmostEqual(engine.get_standard_deviation(is_sample=False), (2/3) ** 0.5)

    def test_empty(self):
        with self.assertRaises(ValueError):
            StatEngine([])

    def test_invalid_type(self):
        with self.assertRaises(TypeError):
            StatEngine([1, 2, "3"])