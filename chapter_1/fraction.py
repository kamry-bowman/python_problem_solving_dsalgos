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
        self.num = top
        self.den = bottom

    def __str__(self):
        return str(self.num) + "/" + str(self.den)

    def __add__(self, arg):
        common = gcd(self.den, arg.den)
        num1 = self.num // (self.den // common)
        num2 = arg.num // (arg.den // common)
        top = num1 + num2
        return Fraction(top, common)

    def __eq__(self, arg):
        num_this = self.num * arg.den
        num_that = arg.num * self.den
        return num_this == num_that


class TestFraction(unittest.TestCase):
    def test_addition(self):
        ex1 = Fraction(3, 5)
        ex2 = Fraction(2, 10)
        sum = ex1 + ex2

        self.assertEqual(sum, Fraction(4, 5))


if __name__ == '__main__':
    unittest.main()
