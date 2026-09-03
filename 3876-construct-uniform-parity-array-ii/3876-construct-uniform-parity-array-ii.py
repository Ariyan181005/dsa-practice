class Solution(object):
    def uniformArray(self, nums1):
        """
        :type nums1: List[int]
        :rtype: bool
        """
        """
        mo = float('inf')
        for x in nums1:
            if x % 2 != 0:
                mo = min(mo, x)
        if mo == float('inf'):
            return True
        for x in nums1:
            if x % 2 == 0 and x < mo:
                return False
        return True
        """
        min_val = min(nums1)
        if min_val % 2 != 0:
            return True
        return all(x % 2 == 0 for x in nums1)