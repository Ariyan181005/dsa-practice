class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        c=[]
        p=0
        k=0
        while p<len(nums):
            if nums[p]!=val:
                nums[k]=nums[p]
                k+=1
            p+=1
        return k