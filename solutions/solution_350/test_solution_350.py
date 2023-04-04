import unittest
from .solution_350 import Solution350

class TestSolution350(unittest.TestCase):
    def test_intersect(self):
        test_cases = [
            ( [1,2,2,1], [2,2], [2,2] ),
            ( [4,9,5], [9,4,9,8,4], [9,4])
        ]
        
        solution = Solution350()
        
        for test_case in test_cases:
            arg1 = test_case[0]
            arg2 = test_case[1]
            expected = test_case[2]
            result = solution.intersect(arg1, arg2)
            self.assertEqual(expected, result)