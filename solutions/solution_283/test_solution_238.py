import unittest
from .solution_238 import Solution238

class TestSolution238(unittest.TestCase):
    def test_move_zeroes(self):
        test_case = [0, 1, 0, 3, 12]
        
        solution = Solution238()
        solution.move_zeroes(test_case)

        self.assertEqual(test_case, [1,3,12,0,0])