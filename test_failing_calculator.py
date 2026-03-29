"""Unit tests for failing_calculator module."""

import unittest
from failing_calculator import average_ratios


class TestAverageRatios(unittest.TestCase):
    """Test cases for average_ratios function."""

    def test_calculate_with_positive_numbers(self):
        """Test normal calculation with positive numbers."""
        result = average_ratios([10, 5, 2])
        # 100/10 = 10, 100/5 = 20, 100/2 = 50
        # Average = (10 + 20 + 50) / 3 = 80 / 3 ≈ 26.67
        expected = (10 + 20 + 50) / 3
        self.assertAlmostEqual(result, expected, places=2)

    def test_single_number(self):
        """Test with single number."""
        result = average_ratios([10])
        # 100/10 = 10
        self.assertEqual(result, 10.0)

    def test_negative_numbers(self):
        """Test with negative numbers."""
        result = average_ratios([-10, -5])
        # 100/-10 = -10, 100/-5 = -20
        # Average = (-10 + -20) / 2 = -15
        expected = (-10 + -20) / 2
        self.assertEqual(result, expected)

    def test_zero_value_raises_error(self):
        """Test that zero value raises ValueError."""
        with self.assertRaises(ValueError) as context:
            average_ratios([10, 5, 0])
        self.assertIn("zero", str(context.exception).lower())

    def test_empty_list_raises_error(self):
        """Test that empty list raises ValueError."""
        with self.assertRaises(ValueError):
            average_ratios([])

    def test_multiple_zeros_raises_error(self):
        """Test that multiple zeros are detected."""
        with self.assertRaises(ValueError):
            average_ratios([10, 0, 0])

    def test_non_numeric_values_raise_error(self):
        """Test that non-numeric values raise TypeError."""
        with self.assertRaises(TypeError):
            average_ratios([10, "five", 2])

    def test_large_numbers(self):
        """Test with large numbers."""
        result = average_ratios([1000, 100])
        # 100/1000 = 0.1, 100/100 = 1.0
        # Average = (0.1 + 1.0) / 2 = 0.55
        expected = (0.1 + 1.0) / 2
        self.assertAlmostEqual(result, expected, places=2)

    def test_float_numbers(self):
        """Test with float numbers."""
        result = average_ratios([2.5, 5.0])
        # 100/2.5 = 40, 100/5.0 = 20
        # Average = (40 + 20) / 2 = 30
        expected = (40 + 20) / 2
        self.assertEqual(result, expected)


if __name__ == '__main__':
    unittest.main()
