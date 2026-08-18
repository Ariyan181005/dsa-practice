class Solution(object):
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        res=[]
        def rec(st):
            if st==len(nums):
                res.append(nums[:])
                return
            for i in range(st,len(nums)):
                nums[st],nums[i]=nums[i],nums[st]
                rec(st+1)
                nums[st],nums[i]=nums[i],nums[st]
        rec(0)
        return res