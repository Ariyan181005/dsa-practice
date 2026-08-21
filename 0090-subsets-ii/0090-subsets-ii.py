class Solution(object):
    def subsetsWithDup(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        nums.sort()
        ans=[]
        def bt(st,path):
            ans.append(path[:])
            for i in range(st,len(nums)):
                if i>st and nums[i]==nums[i-1]:
                    continue
                path.append(nums[i])
                bt(i+1,path)
                path.pop()
        bt(0,[])
        return ans