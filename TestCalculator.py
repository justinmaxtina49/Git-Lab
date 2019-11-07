#master

#示範Git用的程式碼！

#import python的unittest
import unittest
import Calculator as calculator
class TestCalculator(unittest.TestCase):
    def test_int_r(self):
        self.assertEqual(calculator.r(12), 12)

    def test_int2_r(self):
        self.assertEqual(calculator.r(13), 13)

    def test_float_r(self):
        self.assertEqual(calculator.r(7.2), 7.2)

    def test_int_r(self):
        self.assertEqual(calculator.r(6), 6)

    def test_int2_r(self):
        self.assertEqual(calculator.r(5), 5)

    def test_float_r(self):
        self.assertEqual(calculator.r(1.0), 1.0)

    def test_int_r(self):
        self.assertEqual(calculator.r(27), 27)

    def test_int2_r(self):
        self.assertEqual(calculator.r(36), 36)

    def test_float_r(self):
        self.assertEqual(calculator.r(13.86), 13.86)

    def test_int_r(self):
        self.assertEqual(calculator.r(3), 3)

    def test_float_r(self):
        self.assertEqual(calculator.r(1.8), 1.8)

if __name__ == '__main__':
    unittest.main()