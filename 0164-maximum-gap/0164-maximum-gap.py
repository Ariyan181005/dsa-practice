class Solution(object):
    def maximumGap(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        """
        if len(nums)<2:
            return 0
        nums.sort()
        ans=0
        for i in range(1,len(nums)):
            ans=max(ans,nums[i]-nums[i-1])
        return ans
        """
        diff,n=0,sorted(set(nums))
        for i in range(len(n)-1):
            if n[i+1]-n[i] > diff:
                diff = n[i+1] - n[i]
        return(diff)