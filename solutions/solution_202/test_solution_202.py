import unittest
from .solution_202 import Solution202

class TestSolution202(unittest.TestCase):
    def test_is_happy(self):
        test_cases = [
            (19, True),
            (2, False)
        ]
        
        solution = Solution202()
        for test_case in test_cases:
            arg = test_case[0]
            expected = test_case[1]
            result = solution.is_happy(arg)
            self.assertEqual(expected, result)
            