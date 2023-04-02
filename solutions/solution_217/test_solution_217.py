import unittest
from .solution_217 import Solution217

class TestSolution217(unittest.TestCase):
    def test_contains_duplicate(self):
        test_cases = [
            ([1,2,3], False),
            ([1,2,1], True),
            ([1,1,1], True),
            ([-1,1,1,1,1,1,1,1,1,1,1,-1], True)
        ]
        solution217 = Solution217()
        
        for nums, expected in test_cases:
            result = solution217.contains_duplicate(nums)
            self.assertEqual(result, expected)

