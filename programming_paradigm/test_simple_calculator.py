import unittest

class TestCal(unittest.TestCase):
    
    def setUp(self):
        self.calculator = Cal()
    
    def test_add(self):
        self.assertEqual(self.calculator.add(-1, -5), -6)
        
    def test_subtract(self):
        self.assertEqual(self.calculator.subtract(1, -4), 5)
        
    def test_multiply(self):
        self.assertEqual(self.calculator.multiply(5, -3), -15)

    def test_divide(self):
        self.assertEqual(self.calculator.divide(12, -4), -3)
        
if __name__ == "__main__":
  unittest.main()
