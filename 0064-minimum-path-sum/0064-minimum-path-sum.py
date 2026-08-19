class Solution(object):
    def minPathSum(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        m = len(grid)
        n = len(grid[0])
        memo = {}
        def solve(i, j):
            if i >= m or j >= n:
                return float('inf')
            if i == m - 1 and j == n - 1:
                return grid[i][j]
            if (i, j) in memo:
                return memo[(i, j)]
            down = solve(i + 1, j)
            right = solve(i, j + 1)
            memo[(i, j)] = grid[i][j] + min(down, right)
            return memo[(i, j)]
        return solve(0, 0)