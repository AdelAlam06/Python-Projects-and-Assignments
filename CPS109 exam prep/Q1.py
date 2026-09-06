import unittest
"""
Question 1: Swap Elements in a Tuple

Write a function that swaps the first and last elements of a given tuple.
If the tuple has fewer than two elements, return it unchanged.
"""


def swap_first_last(tup):

    if (len(tup) > 2):
        temp = tup[0]
        temp1 = tup[1:-1]
        temp2 = tup[-1]
        return (temp2,)+temp1+(temp,)

    return tup


class TestSwapFirstLast(unittest.TestCase):

    def test_swap_first_last(self):
        # Test case 1: Swap first and last elements in a tuple
        self.assertEqual(swap_first_last((1, 2, 3, 4)), (4, 2, 3, 1))

    def test_single_element_tuple(self):
        # Test case 2: Tuple with a single element (should return the same tuple)
        self.assertEqual(swap_first_last((5,)), (5,))

    def test_empty_tuple(self):
        # Test case 3: Empty tuple (should return the same empty tuple)
        self.assertEqual(swap_first_last(()), ())


if __name__ == '__main__':
    unittest.main(exit=True)
