import unittest


def gcd(num1, num2):

    high = max(num1, num2)
    low = min(num1, num2)

    remainder = high % low

    while(remainder > 0):
        high = low
        low = remainder
        remainder = high % low

    return low


class Fraction:
    def __init__(self, top, bottom):
        common = gcd(top, bottom)
        self.num = top // common
        self.den = bottom // common

    def __str__(self):
        return str(self.num) + "/" + str(self.den)

    def __add__(self, arg):
        num1 = self.num * arg.den
        num2 = arg.num * self.den
        top = num1 + num2
        bottom = self.den * arg.den
        return Fraction(top, bottom)

    def __sub__(self, arg):
        num1 = self.num * arg.den
        num2 = arg.num * self.den

        if (num1 < num2):
            raise Exception('Negative no good')

        top = num1 - num2
        bottom = self.den * arg.den
        return Fraction(top, bottom)

    def __eq__(self, arg):
        num_this = self.num * arg.den
        num_that = arg.num * self.den
        return num_this == num_that

    def __lt__(self, arg):
        num_this = self.num * arg.den
        num_that = arg.num * self.den
        return num_this < num_that

    def __gt__(self, arg):
        num_this = self.num * arg.den
        num_that = arg.num * self.den
        return num_this > num_that

    def __mul__(self, arg):
        top = self.num * arg.num
        bottom = self.den * arg.den
        return Fraction(top, bottom)

    def __div__(self, arg):
        top = self.num * arg.den
        bottom = self.den * arg.num
        return Fraction(top, bottom)

    def __floordiv__(self, arg):
        return self.__div__(arg)


class TestFraction(unittest.TestCase):
    def test_addition(self):
        ex1 = Fraction(3, 5)
        ex2 = Fraction(2, 10)
        sum = ex1 + ex2

        self.assertEqual(sum, Fraction(4, 5))

    def test_subtract(self):
        ex1 = Fraction(3, 5)
        ex2 = Fraction(2, 10)
        difference = ex1 - ex2

        self.assertEqual(difference, Fraction(2, 5))

    def test_subtract_error(self):
        ex1 = Fraction(2, 10)
        ex2 = Fraction(3, 5)

        with self.assertRaises(Exception):
            ex1 - ex2

    def test_rounding(self):
        ex = Fraction(6, 10)
        self.assertEqual(str(ex), "3/5")

    def test_multiply(self):
        ex1 = Fraction(3, 5)
        ex2 = Fraction(2, 10)
        product = ex1 * ex2

        self.assertEqual(product, Fraction(3, 25))

    def test_divide(self):
        ex1 = Fraction(1, 4)
        ex2 = Fraction(20, 50)
        quotient = ex1 // ex2

        self.assertEqual(quotient, Fraction(5, 8))

    def test_gt(self):
        ex1 = Fraction(20, 50)
        ex2 = Fraction(1, 4)

        self.assertTrue(ex1 > ex2)

    def test_lt(self):
        ex1 = Fraction(1, 50)
        ex2 = Fraction(1, 4)

        self.assertTrue(ex1 < ex2)


if __name__ == '__main__':
    unittest.main()
