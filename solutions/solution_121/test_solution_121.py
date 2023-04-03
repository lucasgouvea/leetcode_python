import unittest
from .solution_121 import Solution121

class TestSolution121(unittest.TestCase):
    def test_max_profit(self):
        test_cases = [
            ([7,10,5,3,6,4], 3),
            ([7,6,4,3,1], 0)
        ]
        
        solution = Solution121()
        for test_case in test_cases:
            arg = test_case[0]
            expected = test_case[1]
            result = solution.max_profit(arg)
            self.assertEqual(expected, result)