class Solution(object):
    def minimumDeletions(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        mn = nums.index(min(nums))
        mx = nums.index(max(nums))
        if mn > mx:
            mn, mx = mx, mn
        lt = mx + 1
        rt = n - mn
        b = (mn + 1) + (n - mx)
        return min(lt, rt, b)