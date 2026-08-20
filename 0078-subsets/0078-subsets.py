class Solution(object):
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        res = [[]]
        for i in nums:
            n = []
            for j in res:
                n.append(j + [i])
            res.extend(n)
        return res