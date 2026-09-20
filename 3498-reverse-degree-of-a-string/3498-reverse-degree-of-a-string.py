class Solution:
    def reverseDegree(self, s: str) -> int:
        ans=0
        for i in range (len(s)):
            revind = 26 - (ord(s[i]) - ord('a'))
            ans+=revind*(i+1)
        return ans