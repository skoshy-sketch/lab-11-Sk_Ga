import unittest
from calculator import *

class TestCalculator(unittest.TestCase):
    ######### Partner 2
    def test_add(self): # 3 assertions
         calc = Calculator()
         self.assertEqual(calc.add(2, 3), 5)
         self.assertEqual(calc.add(10, 5), 15)
         self.assertEqual(calc.add(-2, 2), 0)

    def test_subtract(self): # 3 assertions
        calc = Calculator()
        self.assertEqual(calc.subtract(5, 3), 2)
        self.assertEqual(calc.subtract(10, 5), 5)
        self.assertEqual(calc.subtract(2, 5), -3)

    ######## Partner 1
    # def test_multiply(self): # 3 assertions
    #     fill in code

    # def test_divide(self): # 3 assertions
    #     fill in code
    # ##########################

    ######## Partner 2
    def test_divide_by_zero(self): # 1 assertion
        with self.assertRaises(ZeroDivisionError):
        div(0, 5)

    def test_logarithm(self): # 3 assertions
        self.assertEqual(log(1, 10), 0)
        self.assertEqual(log(100, 10), 2)
        self.assertEqual(log(8, 2), 3)

    def test_log_invalid_base(self): # 1 assertion
        with self.assertRaises(ValueError):
        log(10, 1)
    
    ######## Partner 1
    # def test_log_invalid_argument(self): # 1 assertion
    #     # call log function inside, example:
    #     # with self.assertRaises(<INSERT_ERROR_TYPE>):
    #     #     logarithm(0, 5)
    #     fill in code

    # def test_hypotenuse(self): # 3 assertions
    #     fill in code

    # def test_sqrt(self): # 3 assertions
    #     # Test for invalid argument, example:
    #     # with self.assertRaises(<INSERT_ERROR_TYPE>):
    #     #    square_root(NUM)
    #     # Test basic function
    #     fill in code
    ##########################

# Do not touch this
if __name__ == "__main__":
    unittest.main()