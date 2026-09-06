import unittest
"""
Write a function that takes a 2D array (list of lists) of integers and:

    1. Returns the maximum element in the array.
    2. Returns the position (row and column indices) of the maximum element.
"""


def find_max_in_2d_array(matrix):
    maxVal = 0
    x = 0
    cord = ()
    for i in matrix:
        for j in range(len(i)):
            if (i[j] > maxVal):
                maxVal = i[j]
                cord = x, j
        x += 1
    return maxVal, cord


class TestFindMaxIn2DArray(unittest.TestCase):

    def test_find_max_in_2d_array(self):
        array = [
            [1, 2, 3],
            [4, 5, 6],
            [7, 8, 9]
        ]
        max_value, max_position = find_max_in_2d_array(array)
        self.assertEqual(max_value, 9)
        self.assertEqual(max_position, (2, 2))


if __name__ == '__main__':
    unittest.main(exit=True)
