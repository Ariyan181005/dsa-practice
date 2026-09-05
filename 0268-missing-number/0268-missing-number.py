class Solution(object):
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        """
        ma=max(nums)
        mi=min(nums)
        for i in range(mi,ma):
            if i not in nums:
                return i
        if mi != 0:
            return 0
        return ma + 1
        """
        n= len(nums)
        total = n * (n + 1) //2
        return total - sum(nums)