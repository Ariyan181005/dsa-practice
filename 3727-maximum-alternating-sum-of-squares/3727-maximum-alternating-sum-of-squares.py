class Solution:
    def maxAlternatingSum(self, nums: List[int]) -> int:
        nums.sort(key=lambda x: x * x)
        n = len(nums)
        a = sum(x * x for x in nums[:n // 2])
        b = sum(x * x for x in nums[n // 2:])
        return b - a