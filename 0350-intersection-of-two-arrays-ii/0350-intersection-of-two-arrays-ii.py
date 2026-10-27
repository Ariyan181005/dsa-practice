from collections import Counter
from typing import List
class Solution:
    def intersect(self, nums1: list[int], nums2: list[int]) -> list[int]:
        freq = Counter(nums1)
        result = []
        for num in nums2:
            if freq[num] > 0:
                result.append(num)
                freq[num] -= 1
        return result