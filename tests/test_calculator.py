import unittest
from src.calculator import sum, substract, multiply, divide

class CalculatorTests(unittest.TestCase):
    
    def test_sum(self):
        assert sum(2,3) == 5
    
    def test_substract(self):
        assert substract(10,5) == 5
    
    def test_multiply(self):
        assert multiply(3,3) == 9
    
    def test_divide(self):
        assert divide(10, 2) == 5
    
    def test_divide_by_zero(self):
        with self.assertRaises(ZeroDivisionError):
            divide(10,0)