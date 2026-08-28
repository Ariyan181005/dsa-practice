class Solution(object):
    def findRepeatedDnaSequences(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        se=set()
        ans=set()
        for i in range(len(s)-9):
            x=s[i:i+10]
            if x in se:
                ans.add(x)
            else:
                se.add(x)
        return list(ans)