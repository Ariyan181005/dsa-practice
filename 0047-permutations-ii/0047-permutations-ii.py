class Solution(object):
    def permuteUnique(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        res=[]
        def rec(st):
            if st==len(nums):
                if nums[:] not in res:
                    res.append(nums[:])
                return
            for i in range(st,len(nums)):
                nums[st],nums[i]=nums[i],nums[st]
                rec(st+1)
                nums[st],nums[i]=nums[i],nums[st]
        rec(0)
        return res