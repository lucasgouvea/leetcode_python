from typing import List, Dict

class Solution217:
    def __init__(self) -> None:
        pass
    def contains_duplicate(self, nums: List[int]) -> bool:
        nums_count: Dict[str, int] = {}
        for num in nums:
            count = nums_count.get(num)
            if count == None:
                nums_count[num] = 1
            if count == 1:
                return True
        return False