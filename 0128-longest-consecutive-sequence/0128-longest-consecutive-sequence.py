class Solution(object):
    def longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        s = set(nums)
        l = 0
        for i in s:
            if i - 1 not in s:
                count = 1
                while i + count in s:
                    count += 1
                l = max(l, count)
        return l