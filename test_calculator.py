# https://github.com/zmckirdy/lab11-ZM-AN.git
# Partner 1: Zach McKirdy
# Partner 2: Aditya Nair

import unittest
from calculator import *

class TestCalculator(unittest.TestCase):
    ######### Partner 2
    # def test_add(self): # 3 assertions
    #     fill in code

    # def test_subtract(self): # 3 assertions
    #     fill in code
    # ##########################

    ######## Partner 1
    def test_multiply(self): # 3 assertions
        self.assertEqual(mul(5, 10), 50)
        self.assertEqual(mul(7, 0), 0)
        self.assertAlmostEqual(mul(0.5, 0.1), 0.05, places=7)

    def test_divide(self): # 3 assertions
        self.assertEqual(div(2, 8), 4)
        self.assertAlmostEqual(div(2, 5), 2.5, places=7)
        with self.assertRaises(ZeroDivisionError):
            div(0, 1)
    # ##########################

    ######## Partner 2
    # def test_divide_by_zero(self): # 1 assertion
    #     # call division function inside, example:
    #     # with self.assertRaises(<INSERT_ERROR_TYPE>):
    #     #     div(0, 5)
    #     fill in code

    # def test_logarithm(self): # 3 assertions
    #     fill in code

    # def test_log_invalid_base(self): # 1 assertion
    #     # use same technique from test_divide_by_zero
    #     fill in code
    # ##########################
    
    ######## Partner 1
    def test_log_invalid_argument(self): # 1 assertion
        # call log function inside, example:
        # with self.assertRaises(<INSERT_ERROR_TYPE>):
        #     logarithm(0, 5)
        with self.assertRaises(ValueError):
            logarithm(0, 5)

    def test_hypotenuse(self): # 3 assertions
        self.assertEqual(hypotenuse(3, 4), 5)
        self.assertEqual(hypotenuse(0, 0), 0)
        self.assertEqual(hypotenuse(-6, -8), 10)

    def test_sqrt(self): # 3 assertions
        # Test for invalid argument, example:
        # with self.assertRaises(<INSERT_ERROR_TYPE>):
        #    square_root(NUM)
        # Test basic function
        self.assertEqual(square_root(100), 10)
        self.assertAlmostEqual(square_root(5), 5 ** 0.5, places=7)
        with self.assertRaises(ValueError):
            square_root(-49)
    ##########################

# Do not touch this
if __name__ == "__main__":
    unittest.main()