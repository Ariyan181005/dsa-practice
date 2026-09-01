class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        """
        # normal way
        s=set()
        for i in nums:
            if i in s:
                return True
            s.add(i)
        return False
        """
        #easiest way
        return len(nums)!=len(set(nums))