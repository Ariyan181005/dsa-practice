class Solution:
    def resultArray(self, nums: List[int], k: int) -> List[int]:
        ans = [0] * k
        dp = [0] * k
        for num in nums:
            new = [0] * k
            x = num % k
            new[x] += 1
            for r in range(k):
                nr = (r * x) % k
                new[nr] += dp[r]
            for r in range(k):
                ans[r] += new[r]
            dp = new
        return ans