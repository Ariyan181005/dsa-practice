class Solution(object):
    def lexicographicallySmallestArray(self, nums, limit):
        """
        :type nums: List[int]
        :type limit: int
        :rtype: List[int]
        """
        n = len(nums)
        a = sorted((v, i) for i, v in enumerate(nums))
        ans = nums[:]
        l = 0
        while l < n:
            r = l
            while r + 1 < n and a[r + 1][0] - a[r][0] <= limit:
                r += 1
            inds = sorted(a[i][1] for i in range(l, r + 1))
            vals = [a[i][0] for i in range(l, r + 1)]
            for i in range(len(inds)):
                ans[inds[i]] = vals[i]
            l = r + 1
        return ans