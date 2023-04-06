from typing import Optional
from structures.structures import ListNode


class Solution160:
    class NodeCount:
        def __init__(self, value: int, count: int) -> None:
            self.value = value
            self.count = count
        def increment_count(self) -> None:
            self.count += 1
    def get_intersection_node(self, head_a: ListNode, head_b: ListNode) -> Optional[ListNode]:
        memory_address_node_count: dict[str, self.NodeCount] = {}
        ptr_a = head_a
        ptr_b = head_b
        
        while(ptr_a is not None or ptr_b is not None):
            if ptr_a is not None:
                addr = self.get_memory_address(ptr_a)
                node_count = memory_address_node_count.get(addr)
                if node_count is None:
                    memory_address_node_count[addr] = self.NodeCount(ptr_a.val, 1)
                else:
                    return ptr_a
                ptr_a = ptr_a.next
            if ptr_b is not None:
                addr = self.get_memory_address(ptr_b)
                node_count = memory_address_node_count.get(addr)
                if node_count is None:
                    memory_address_node_count[addr] = self.NodeCount(ptr_b.val, 1)
                else:
                    return ptr_b
                ptr_b = ptr_b.next

        return None

    def get_memory_address(self, node: ListNode) -> str:
        return hex(id(node))