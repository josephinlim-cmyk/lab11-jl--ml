#https://github.com/josephinlim-cmyk/lab11-jl--ml
#Partner 1: Josephine Lim
#Partner 2: Miaohan Lin

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
        positive = 6
        gotpositive = mul(2, 3)
        self.assertEqual(positive, gotpositive)

        posandneg = -6
        gotmixed = mul(2, -3)
        self.assertEqual(posandneg, gotmixed)

        negative = 6
        gotnegative = mul(-2, -3)
        self.assertEqual(negative, gotnegative)



    def test_divide(self): # 3 assertions
        positive = 2
        gotpositive = div(3, 6)
        self.assertEqual(positive, gotpositive)

        posandneg = -2
        gotmixed = div(3, -6)
        self.assertEqual(posandneg, gotmixed)

        negative = 2
        gotnegative = div(-3, -6)
        self.assertEqual(negative, gotnegative)

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
            logarithm(0, 5)

    def test_hypotenuse(self): # 3 assertions
        positive = 5
        gotpositive = hypotenuse(3, 4)
        self.assertAlmostEqual(positive, gotpositive)

        posandneg = 5
        gotmixed = hypotenuse(3, -4)
        self.assertAlmostEqual(posandneg, gotmixed)

        negative = 5
        gotnegative = hypotenuse(-3, -4)
        self.assertAlmostEqual(negative, gotnegative)


    def test_sqrt(self): # 3 assertions
        with self.assertRaises(ValueError):
            square_root(-9)

        zero = square_root(0)
        self.assertAlmostEqual(zero, 0)

        nine = square_root(9)
        self.assertAlmostEqual(nine, 3)

# Do not touch this
if __name__ == "__main__":
    unittest.main()