import unittest
"""
Question 2: Tuple Subtraction

Write a Python function named tuple_subtraction that takes a list of tuples as input.
Each tuple contains two or more integers. The function should return a list of results,
where each result is the subtraction of the elements in the corresponding tuple,
computed from left to right.
"""


def tuple_subtraction(tuples_list):
    diffList = []
    for i in tuples_list:
        diff = i[0]
        for j in i[1:]:
            diff -= j
        diffList.append(diff)
    return diffList


class TestTupleSubtraction(unittest.TestCase):

    def test_tuple_subtraction(self):
        # Test case: Subtract all elements in each tuple from the first element
        tuples_list = [
            (10, 3, 2),
            (20, 5, 5),
            (8, 3),
            (4,)
        ]
        result = tuple_subtraction(tuples_list)
        self.assertEqual(result, [5, 10, 5, 4])


if __name__ == '__main__':
    unittest.main(exit=True)
