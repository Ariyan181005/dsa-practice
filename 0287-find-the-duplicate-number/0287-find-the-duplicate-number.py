class Solution(object):
    def findDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        """
        s = nums[0]
        f = nums[0]
        while True:
            s = nums[s]
            f = nums[nums[f]]
            if s == f:
                break
        s = nums[0]
        while s != f:
            s = nums[s]
            f = nums[f]
        return s
        """
        n=len(nums)
        s=set()
        for x in nums:
            if x in s:
                return x
            else:
                s.add(x)