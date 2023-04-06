import unittest
from structures.structures import ListNode
from .solution_160 import Solution160


class TestSolution160(unittest.TestCase):
    def test_get_intersection_node(self):
        a1 = ListNode(4)
        a2 = ListNode(1)
        b1 = ListNode(5)
        b2 = ListNode(6)
        b3 = ListNode(1)
        c1 = ListNode(8)
        c2 = ListNode(4)
        c3 = ListNode(5)
        
        a1.next = a2
        a2.next = c1
        
        b1.next = b2
        b2.next = b3
        b3.next = c1
        
        c1.next = c2
        c2.next = c3
        
        sol = Solution160()
        result = sol.get_intersection_node(a1, b1)
        self.assertEqual(result, c1)