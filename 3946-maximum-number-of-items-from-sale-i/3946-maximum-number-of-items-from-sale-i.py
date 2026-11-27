class Solution:
    def maximumSaleItems(self, items: List[List[int]], budget: int) -> int:
        n = len(items)
        dp = [0] * (budget + 1)
        mn = float('inf')
        for i in range(n):
            factor, price = items[i]
            mn = min(mn, price)
            cnt = 0
            for j in range(n):
                if i != j and items[j][0] % factor == 0:
                    cnt += 1
            for j in range(budget, price - 1, -1):
                dp[j] = max(dp[j], dp[j - price] + cnt + 1)
        ans = 0
        for i in range(budget + 1):
            ans = max(ans, dp[i] + (budget - i) // mn)
        return ans
