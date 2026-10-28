class Solution:
    def minCost(self, grid: list[list[int]]) -> int:
        m, n = len(grid), len(grid[0])
        BITS = 1024

        dp = [[False] * BITS for _ in range(n)]
        dp[0][grid[0][0]] = True

        for i in range(m):
            for j in range(n):
                if i == 0 and j == 0:
                    continue

                value = grid[i][j]
                curr = [False] * BITS

                if i > 0:
                    for x in range(BITS):
                        if dp[j][x]:
                            curr[x ^ value] = True

                if j > 0:
                    for x in range(BITS):
                        if dp[j - 1][x]:
                            curr[x ^ value] = True

                dp[j] = curr

        for x in range(BITS):
            if dp[n - 1][x]:
                return x

        return -1