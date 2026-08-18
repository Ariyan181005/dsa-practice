class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        """
        l=[]
        s=0
        for i in range(len(nums)):
            for j in range(i, len(nums)):
                l.append(nums[i:j+1])
        for i in l:
            if sum(i)>=s:
                s=sum(i)
        return s
        """
        s = nums[0]
        curr = nums[0]
        for i in range(1, len(nums)):
            curr = max(nums[i], curr + nums[i])
            s = max(s, curr)
        return s