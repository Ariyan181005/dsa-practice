class Solution(object):
    def containsNearbyDuplicate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        
        a={}
        for i in range(len(nums)):
            if nums[i] in a :
                if i - a[nums[i]] <= k:
                    return True
            a[nums[i]] = i
        return False