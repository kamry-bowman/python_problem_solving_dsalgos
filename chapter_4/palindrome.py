import unittest
import re


letters_re = re.compile(r'[A-Z]', flags=re.I)


def palindrome(string):
    if string == '':
        return True

    def help(l, r):
        if l == r:
            return True

        elif letters_re.search(string[l]) is None:
            return help(l + 1, r)

        elif letters_re.search(string[r]) is None:
            return help(l, r - 1)

        elif l + 1 == r:
            return string[l] == string[r]

        else:
            if string[l] != string[r]:
                return False
            return help(l + 1, r - 1)

    return help(0, len(string) - 1)


class MyTest(unittest.TestCase):
    def test_empty(self):
        self.assertEqual(palindrome(''), True)

    def test_one_good(self):
        self.assertEqual(palindrome('a'), True)

    def test_two_good(self):
        self.assertEqual(palindrome('aa'), True)

    def test_two_bad(self):
        self.assertEqual(palindrome('ab'), False)

    def test_three_bad(self):
        self.assertEqual(palindrome('abb'), False)

    def test_three_good(self):
        self.assertEqual(palindrome('aba'), True)

    def test_three_good_punc(self):
        self.assertEqual(palindrome('a b-a'), True)

    def test_three_bad_punc(self):
        self.assertEqual(palindrome('a-b- b'), False)


if __name__ == '__main__':
    unittest.main()
