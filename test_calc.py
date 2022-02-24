import unittest
import calc


class TestCalc(unittest.TestCase):
    def test_sum(self):
        result = calc.sum(3, 7)
        self.assertEqual(10, result)

    def test_minus(self):
        result = calc.minus(7, 3)
        self.assertEqual(4, result)
