
import unittest

"""
Question 4: Sum of Digits Using Recursion

Write a recursive function to calculate the sum of the digits of a positive integer.
"""


def sum_of_digits(n):
    num = str(n)
    if (n == 0):
        return 0
    else:
        return int(num[-1]) + sum_of_digits(n//10)


class TestSumOfDigits(unittest.TestCase):

    # Test Case 1: Sum of digits for 1234
    def test_sum_of_digits_1234(self):
        self.assertEqual(sum_of_digits(1234), 10)

    # Test Case 2: Sum of digits for 7 (a single digit number)
    def test_sum_of_digits_7(self):
        self.assertEqual(sum_of_digits(7), 7)

    # Test Case 3: Sum of digits for 1234 again, testing multiple scenarios
    def test_sum_of_digits_repeated(self):
        self.assertEqual(sum_of_digits(1234), 10)


if __name__ == '__main__':
    unittest.main(exit=True)
