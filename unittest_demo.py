import unittest

class Calculator:
    def multi(self, multiplier,multiplicand):
        product = multiplier * multiplicand
        return product

class CalculatorTest(unittest.TestCase):

    def test_multi(self):
        cal = Calculator()
        self.assertEqual(cal.multi(10, 2), 20)

if __name__ == '__main__':
    unittest.main()
