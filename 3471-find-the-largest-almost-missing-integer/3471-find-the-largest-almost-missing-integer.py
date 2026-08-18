class Solution(object):
    def largestInteger(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        n = len(nums)
        if k == 1:
            ans = -1
            for x in nums:
                if nums.count(x) == 1:
                    ans = max(ans, x)
            return ans
        if k == n:
            return max(nums)
        ans = -1
        if nums.count(nums[0]) == 1:
            ans = max(ans, nums[0])
        if nums.count(nums[-1]) == 1:
            ans = max(ans, nums[-1])
        return ans        