class Solution:
    def maxAlternatingSum(self, nums: List[int]) -> int:
        a = [x * x for x in nums]
        a.sort()
        n = len(a)
        b = (n + 1) // 2
        c = n // 2
        d = sum(a[:c])
        e = sum(a[c:])
        return e - d