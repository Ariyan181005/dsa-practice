class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        xor=0
        for i in nums:
            xor ^= i
        d=xor & -xor
        a=b=0
        for i in nums:
            if i & d:
                a^=i
            else:
                b^=i
        return [a,b]