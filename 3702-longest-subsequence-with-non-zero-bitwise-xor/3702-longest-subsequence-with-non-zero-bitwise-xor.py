class Solution(object):
    def longestSubsequence(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        xall=0
        a=False
        for x in nums:
            xall^=x
            if x!=0:
                a=True
        if xall!=0:
            return len(nums)
        elif a:
            return (len(nums)-1)
        else:
            return 0