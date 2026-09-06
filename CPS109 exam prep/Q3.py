import unittest
from unittest.mock import mock_open, patch
"""
Question 3: Count the number of ‘M’s in a file

Write a function that:
    1. takes in a file called ‘pacs_cscu_cafe.txt’
    2. counts the number of occurrences of the letter M (both lowercase and uppercase) in the file.
"""


def countM():
    """Mock file opening and reading"""
    with open("pacs_cscu_cafe.txt", "r") as myFile:
        content = myFile.read()
        totM = content.count("M") + content.count("m")

    return totM


class TestCountM(unittest.TestCase):

    @patch("builtins.open", mock_open(read_data="My Mom Makes Muffins. Mmmm, Muffins are the best."))
    def test_count_m_occurrences(self):
        # Test case: Count occurrences of 'M' in the mocked file content
        self.assertEqual(countM(), 10)


if __name__ == '__main__':
    unittest.main(exit=True)
