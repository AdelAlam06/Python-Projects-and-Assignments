import unittest
"""
Question 7: Divide Two Numbers Safely

Write a function that divides two numbers and handles potential errors:
    1. Raise a “ZeroDivisionError” error if the denominator is zero.
    2. Handle invalid inputs (e.g., if the inputs are not numbers).
    3. Return the result if the division is successful.

Example:
    Input 1: 10, 2
    Output 1: 5.0

    Input 2: 10, 0
    Output 2: "Error: Division by zero is not allowed."

    Input 3: "10", "a"
    Output 3: "Error: Invalid input. Please enter numbers only.
"""


def safe_divide(num1, num2):

    if (num2 == 0):
        return 'Error: Division by zero is not allowed.'
    elif (str(num1).isnumeric() and str(num2).isnumeric()):
        return round(num1/num2, 2)
    else:
        return 'Error: Invalid input. Please enter numbers only.'


class TestSafeDivide(unittest.TestCase):
    """Test cases for safe_divide function."""

    # Test Case 1: Division of two positive numbers
    def test_divide_positive_numbers(self):
        self.assertEqual(safe_divide(10, 2), 5.0)

    # Test Case 2: Division by zero
    def test_divide_by_zero(self):
        self.assertEqual(safe_divide(10, 0),
                         "Error: Division by zero is not allowed.")

    # Test Case 3: Invalid input (string and non-numeric character)
    def test_invalid_input_non_numeric(self):
        self.assertEqual(safe_divide("10", "a"),
                         "Error: Invalid input. Please enter numbers only.")


if __name__ == '__main__':
    unittest.main(exit=True)
