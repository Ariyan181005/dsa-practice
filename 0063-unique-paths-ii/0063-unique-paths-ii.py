class Solution(object):
    def uniquePathsWithObstacles(self,grid):
        """
        :type obstacleGrid: List[List[int]]
        :rtype: int
        """
        m,n,=len(grid),len(grid[0])
        dp=[0]*n
        dp[n-1]=1
        for r in reversed(range(m)):
            for c in reversed(range(n)):
                if grid[r][c]:
                    dp[c]=0
                elif c+1<n:
                    dp[c]=dp[c]+dp[c+1]
        return dp[0]