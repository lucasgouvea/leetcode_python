import unittest
from .solution_125 import Solution125


class TestSolution125(unittest.TestCase):
    def test_is_palindrome(self):
        test_cases = [
            ("A man, a plan, a canal: Panama", True),
            ("race a car", False),
            (" ", True),
            ("0P", False),
        ]
        
        solution = Solution125()
        for test_case in test_cases:
            arg = test_case[0]
            expected = test_case[1]
            result = solution.is_palindrome(arg)
            self.assertEqual(expected, result)