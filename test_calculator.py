# https://github.com/hannahpjohns/lab11-HJ-KR.git
# Partner 1: Hannah Johns
# Partner 2: Kaydence Rao

import unittest
from calculator import *

class TestCalculator(unittest.TestCase):
    ######### Partner 2
    def test_add(self): # 3 assertions
        self.assertEqual(add(1,2), 3)
        self.assertEqual(add(0, 5), 5)
        self.assertEqual(add(-1, -8), -9)

    def test_subtract(self): # 3 assertions
        self.assertEqual(subtract(5,3), 2)
        self.assertEqual(subtract(9,-9), 18)
        self.assertEqual(subtract(-3,2), -5)
    # ##########################

    ######## Partner 1
    def test_multiply(self): # 3 assertions
        self.assertEqual(-1, mul(1, -1))
        self.assertEqual(1, mul(1, 1))
        self.assertEqual(0, mul(1, 0))


    def test_divide(self): # 3 assertions
        self.assertEqual(1, div(1, 1))
        with self.assertRaises(ZeroDivisionError):
            div(0,1)
        self.assertEqual(-1, div(1, -1))

    # ##########################

    ######## Partner 2
    def test_divide_by_zero(self): # 1 assertion
        # call division function inside, example:
        # with self.assertRaises(<INSERT_ERROR_TYPE>):
        #     div(0, 5)
        with self.assertRaises(ZeroDivisionError):
            div(0,5)

    def test_logarithm(self): # 3 assertions
        self.assertEqual(logarithm(2,8),3)
        self.assertEqual(logarithm(3,9),2)
        self.assertEqual(logarithm(2,4),2)

    def test_log_invalid_base(self): # 1 assertion
        # use same technique from test_divide_by_zero
        with self.assertRaises(ValueError):
            logarithm(0,0)
    # ##########################
    
    ######## Partner 1
    def test_log_invalid_argument(self): # 1 assertion
        with self.assertRaises(ValueError):
            logarithm(0, 5)
        with self.assertRaises(ValueError):
            logarithm(-1, 5)
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