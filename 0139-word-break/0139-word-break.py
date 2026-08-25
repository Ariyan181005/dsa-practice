class Solution(object):
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: bool
        """
        dp=[False]*(len(s)+1)
        dp[0]=True
        for i in range(1,len(s)+1):
            for j in wordDict:
                if i>= len(j) and dp[i-len(j)]:
                    if s[i-len(j):i]==j:
                        dp[i]=True
                        break
        return dp[len(s)]