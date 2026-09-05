class Solution(object):
    def hIndex(self, citations):
        """
        :type citations: List[int]
        :rtype: int
        """
        n = len(citations)
        l = 0
        r = n - 1
        while l <= r:
            m = (l + r) // 2
            p = n - m
            if citations[m] >= p:
                r = m - 1
            else:
                l = m + 1
        return n - l