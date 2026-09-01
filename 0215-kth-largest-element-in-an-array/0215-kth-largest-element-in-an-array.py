import numpy as np
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        """
        #with sort
        nums.sort(reverse=True)
        return nums[k-1]
        """
        #without sort
        return int(np.partition(nums, -k)[-k])