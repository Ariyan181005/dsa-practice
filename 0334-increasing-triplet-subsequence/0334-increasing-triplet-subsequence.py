class Solution(object):
    def increasingTriplet(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        """
        for i in range (len(nums)):
            if nums[i]<nums[i+1]<nums[i+2]:
                break
            else:
                return False
        return True
        """
        a=float('inf')
        b=float('inf')
        for i in nums:
            if i <= a:
                a=i
            elif i<= b:
                b=i
            else:
                return True
        return False