class Solution(object):
    def findRepeatedDnaSequences(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        seen=set()
        ans=set()
        for i in range(len(s)-9):
            x=s[i:i+10]
            if x in seen:
                ans.add(x)
            else:
                seen.add(x)
        return list(ans)