import unittest
from simple_calculator import SimpleCalculator

class TestSimpleCalculator(unittest.TestCase):
    
    def setUp(self):
        self.cal = SimpleCalculator()
    
    def test_addition(self):
        self.assertEqual(self.cal.add(-1, -5), -6)
        
    def test_subtract(self):
        self.assertEqual(self.cal.subtract(1, -4), 5)
        
    def test_multiply(self):
        self.assertEqual(self.cal.multiply(5, -3), -15)

    def test_divide(self):
        self.assertEqual(self.cal.divide(12, -4), -3)
        
if __name__ == "__main__":
  unittest.main()
