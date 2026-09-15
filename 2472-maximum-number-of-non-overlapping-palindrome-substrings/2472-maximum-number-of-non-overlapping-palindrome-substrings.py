class Solution:
    def maxPalindromes(self, s: str, k: int) -> int:
        """
        n=len(s)
        pal=[[False]*n for _ in range(n)]
        for i in range (n-1,-1,-1):
            for j in range(i,n):
                if s[i]==s[j]:
                    if j-i<=1:
                        pal[i][j]=True
                    else:
                        pal[i][j]=pal[i+1][j-1]
        dp=[0]*(n+1)
        for i in range(1,n+1):
            dp[i]=dp[i-1]
            for j in range(i):
                l=i-j
                if l >= k and pal[j][i-1]:
                    dp[i]= max(dp[i],dp[j]+1)
        return dp[n]
        """
        n = len(s)
        ans = 0
        le = -1
        for i in range(k - 1, n):
            if i - k + 1 > le and s[i - k + 1 : i + 1] == s[i - k + 1 : i + 1][::-1]:
                ans += 1
                le = i
            elif i - k > le and s[i - k : i + 1] == s[i - k : i + 1][::-1]:
                ans += 1
                le = i
        return ans