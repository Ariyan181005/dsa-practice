class Solution(object):
    def minSubArrayLen(self, target, nums):
        """
        :type target: int
        :type nums: List[int]
        :rtype: int
        """
        lt = 0
        s = 0
        ans = float('inf')
        for rt in range(len(nums)):
            s += nums[rt]
            while s >= target:
                ans = min(ans, rt - lt + 1)
                s -= nums[lt]
                lt += 1
        if ans == float('inf'):
            return 0
        return ans