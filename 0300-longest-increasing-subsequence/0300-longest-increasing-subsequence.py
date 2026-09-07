class Solution(object):
    def lengthOfLIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        s = []
        for n in nums:
            if not s or n > s[-1]:
                s.append(n)
            else:
                idx = bisect_left(s, n)
                s[idx] = n
        return len(s)