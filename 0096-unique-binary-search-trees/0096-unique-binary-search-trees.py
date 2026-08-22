class Solution(object):
    def numTrees(self, n):
        """
        :type n: int
        :rtype: int
        """
        dp=[0]*(n+1)
        dp[0]=1
        dp[1]=1
        for n in range(2,n+1):
            for r in range(1,n+1):
                lt=r-1
                rt=n-r
                dp[n]+=dp[lt]*dp[rt]
        return dp[n]