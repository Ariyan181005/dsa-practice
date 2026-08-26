class Solution(object):
    def maxProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        mx=nums[0]
        mn=nums[0]
        ans=nums[0]
        for i in range(1,len(nums)):
            x=nums[i]
            if x<0:
                mx,mn=mn,mx
            mx=max(x,mx*x)
            mn=min(x,mn*x)
            ans=max(ans,mx)
        return ans