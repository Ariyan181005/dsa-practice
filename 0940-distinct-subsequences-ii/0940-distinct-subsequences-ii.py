class Solution(object):
    def distinctSubseqII(self, s):
        """
        :type s: str
        :rtype: int
        """
        m=10**9 +7
        dp=[0] * (len(s)+1)
        dp[0]=1
        lt={}
        for i in range(1,len(s)+1):
            c=s[i-1]
            dp[i]=2*dp[i-1]
            if c in lt:
                dp[i] -= lt[c]
            dp[i]%=m
            lt[c]=dp[i-1]
        return (dp[len(s)]-1) % m