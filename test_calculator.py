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
        self.assertEqual(-1, mul(1, -1))
        self.assertEqual(1, mul(1, 1))
        self.assertEqual(0, mul(1, 0))


    def test_divide(self): # 3 assertions
        self.assertEqual(1, div(1, 1))
        self.assertRaises(ZeroDivisionError, div(1,0))
        self.assertEqual(-1, div(1, -1))

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
        with self.assertRaises(ValueError):
            log(0, 5)
        with self.assertRaises(ValueError):
            log(-1, 5)
    #     fill in code

    def test_hypotenuse(self): # 3 assertions
        self.assertEqual(5, hypotenuse(3,4))
        self.assertEqual(5, hypotenuse(-3, 4))
        self.assertEqual(5, hypotenuse(-3, -4))

def test_sqrt(self): # 3 assertions
    with self.assertRaises(ValueError):
        square_root(-25)
    self.assertEqual(1, square_root(1))
    self.assertEqual(0, square_root(0))
    #     # Test basic function
    #     fill in code
    ##########################

# Do not touch this
if __name__ == "__main__":
    unittest.main()