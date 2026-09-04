class Solution(object):
    def firstStableIndex(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        n = len(nums)
        rt = [0] * n
        rt[n - 1] = nums[n - 1]
        for i in range(n - 2, -1, -1):
            rt[i] = min(nums[i], rt[i + 1])
        lt = nums[0]
        for i in range(n):
            lt = max(lt, nums[i])
            if lt - rt[i] <= k:
                return i
        return -1