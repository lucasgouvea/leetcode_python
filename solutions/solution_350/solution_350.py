from typing import List


class Solution350:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        num_count: dict[int, int] = {}

        for num in nums1:
            count = num_count.get(num)
            if count == None:
                num_count[num] = 1
            else:
                num_count[num] += 1
        
        list: List[int] = []

        for num in nums2:
            count = num_count.get(num)
            if count != None and count > 0:
                list.append(num)
                num_count[num] -= 1
                
        return list