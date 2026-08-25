class Solution(object):
    def missingMultiple(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        s=set(nums)
        i=1
        while True:
            x=k*i
            if x not in s:
                return x
            i+=1