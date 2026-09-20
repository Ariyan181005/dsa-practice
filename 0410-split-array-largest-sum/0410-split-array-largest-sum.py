class Solution:
    def splitArray(self, nums: list[int], k: int) -> int:
        left = max(nums)
        right = sum(nums)
        while left < right:
            mid = (left + right) // 2
            count = 1
            total = 0
            for i in nums:
                if total + i > mid:
                    count += 1
                    total = i
                else:
                    total += i
            if count <= k:
                right = mid
            else:
                left = mid + 1
        return left