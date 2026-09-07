class Solution(object):
    def findDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n=len(nums)
        s=set()
        for x in nums:
            if x in s:
                return x
            else:
                s.add(x)