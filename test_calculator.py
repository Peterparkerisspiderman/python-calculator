import unittest
from calculator import Calculator

class TestCalculator(unittest.TestCase):

    def setUp(self):
        self.calc = Calculator()

    def test_add(self):
        self.assertEqual(self.calc.add(1, 2), 3)

    # Add the following test methods to the TestCalculator class:
    def test_add_negative(self):
        self.assertEqual(self.calc.add(-1, -2), -3)

    def test_add_zero(self):
        self.assertEqual(self.calc.add(1, 0), 1)

    def test_subtract(self):
        self.assertEqual(self.calc.subtract(1, 2), -1)
        self.assertEqual(self.calc.subtract(4, 8), -4)

    def test_subtract_negative(self):
        self.assertEqual(self.calc.subtract(-1, -1), 0) 
        self.assertEqual(self.calc.subtract(-1, 1), -2) 

    def test_multiply(self):
        self.assertEqual(self.calc.multiply(2, 2), 4)
        self.assertEqual(self.calc.multiply(2, 1), 2)

    def test_multiply_negative(self):
        self.assertEqual(self.calc.multiply(-2, -2), 4) 
        self.assertEqual(self.calc.multiply(-2, 0), 0)

    def test_divide(self):
        self.assertEqual(self.calc.divide(8, 4), 2)
        self.assertEqual(self.calc.divide(10, 5), 2)

    def test_divide_negative(self):
        self.assertEqual(self.calc.divide(-10, 5), -2)  
        self.assertEqual(self.calc.divide(-8, 4), -2)            
    
    def test_modulo(self):
        self.assertEqual(self.calc.modulo(1, 2), 1)
        self.assertEqual(self.calc.modulo(10, 5), 0)

    def test_modulo_negative(self):
        self.assertEqual(self.calc.modulo(-1, -2), -1)
        self.assertEqual(self.calc.modulo(-10, -5), 0)


if __name__ == '__main__':
    unittest.main()