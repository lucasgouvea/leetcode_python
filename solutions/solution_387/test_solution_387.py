import unittest
from .solution_387 import Solution387

class TestSolution387(unittest.TestCase):
    def test_first_uniq_char(self):
        test_cases = [
            ("leetcode", 0),
            ("loveleetcode", 2),
            ("aabb", -1)
        ]
        
        solution = Solution387()
        for test_case in test_cases:
            str = test_case[0]
            expected = test_case[1]
            result = solution.first_uniq_char(str)
            self.assertEqual(expected, result)