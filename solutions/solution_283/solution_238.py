from typing import List


class Solution238:
    def __init__(self) -> None:
        pass
    def move_zeroes(self, nums: List[int]) -> None:
        queue: List[int] = []
        
        for n in nums:
            if n != 0:
                queue.append(n)
                
        for i in range(len(nums)):
            if len(queue) == 0:
                nums[i] = 0
            else:
                nums[i] = queue.pop(0)