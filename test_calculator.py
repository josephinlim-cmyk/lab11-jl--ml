#https://github.com/josephinlim-cmyk/lab11-jl--ml
#Partner 1: Josephine Lim
#Partner 2: Miaohan Lin

import unittest
from calculator import *

class TestCalculator(unittest.TestCase):
    ######### Partner 2
    def test_add(self): # 3 assertions
        self.assertEqual(add(2, 3), 5)
        self.assertEqual(add(-1, 1), 0)
        self.assertEqual(add(0, 0), 0)

    def test_subtract(self): # 3 assertions
        self.assertEqual(sub(5, 3), 2)
        self.assertEqual(sub(0, 5), -5)
        self.assertEqual(sub(-1, -1), 0)

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
    def test_divide_by_zero(self): # 1 assertion
        with self.assertRaises(ZeroDivisionError):
            div(0, 5)
    
    def test_logarithm(self): # 3 assertions
        self.assertAlmostEqual(log(2, 8), 3.0, places=5)
        self.assertAlmostEqual(log(10, 100), 2.0, places=5)
        self.assertAlmostEqual(log(5, 25), 2.0, places=5)

    def test_log_invalid_base(self): # 1 assertion
        with self.assertRaises(ValueError):
            log(0, 5)
    
    ######## Partner 1
    def test_log_invalid_argument(self): # 1 assertion
        with self.assertRaises(ValueError):
            logarithm(0, 5)

    def test_hypotenuse(self): # 3 assertions
        positive = 5
        gotpositive = hypotenuse(3, 4)
        self.assertAlmostEqual(positive, gotpositive)

        posandneg = 5
        gotmixed = mul(3, -4)
        self.assertAlmostEqual(posandneg, gotmixed)

        negative = 5
        gotnegative = mul(-3, -4)
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