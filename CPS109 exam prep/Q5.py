import unittest
"""
Question 5: Analyze a Dictionary of Student Grades

Write a function that takes a dictionary where:
    Keys are student names (strings).
    Values are lists of grades (integers).
    
The function should:
    1. Calculate the average grade for each student and return it in a new dictionary.
    2. Find the student with the highest average grade and return their name.
"""


def analyze_grades(grades_dict):
    newDict = {}

    if (len(grades_dict) == 0):
        return grades_dict
    for key in grades_dict:
        if (grades_dict[key] == None):
            newDict[key] = None
        newDict[key] = round(sum(grades_dict[key]) / len(grades_dict[key]), 2)

    return newDict, max(newDict, key=newDict.get)


class TestAnalyzeGrades(unittest.TestCase):

    # Test Case 1: General case with multiple students and grades
    def test_general_case(self):
        grades = {
            "Alice": [85, 90, 78],
            "Bob": [72, 88, 91],
            "Charlie": [90, 92, 85]
        }

        averages, best_student = analyze_grades(grades)

        self.assertAlmostEqual(averages["Alice"], 84.33, places=2)
        self.assertAlmostEqual(averages["Bob"], 83.67, places=2)
        self.assertAlmostEqual(averages["Charlie"], 89.0, places=2)
        self.assertEqual(best_student, "Charlie")

    # Test Case 2: A single student
    def test_single_student(self):
        grades = {
            "Diana": [100, 90, 95]
        }

        averages, best_student = analyze_grades(grades)

        self.assertEqual(averages["Diana"], 95.0)
        self.assertEqual(best_student, "Diana")

    # Test Case 3: Edge case with no students
    def test_no_students(self):
        grades = {}

        averages, best_student = analyze_grades(grades)

        self.assertEqual(averages, {})
        self.assertIsNone(best_student)

    # Test Case 4: Edge case with students having no grades
    def test_no_grades_for_students(self):
        grades = {
            "Jack": [],
            "Jill": []
        }

        averages, best_student = analyze_grades(grades)

        self.assertIsNone(averages["Jack"])
        self.assertIsNone(averages["Jill"])
        self.assertIsNone(best_student)


if __name__ == '__main__':
    unittest.main(exit=True)
