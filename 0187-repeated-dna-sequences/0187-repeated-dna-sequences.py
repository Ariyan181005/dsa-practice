class Solution(object):
    def findRepeatedDnaSequences(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        """
        seen=set()
        ans=set()
        for i in range(len(s)-9):
            seq=s[i:i+10]
            if seq in seen:
                ans.add(seq)
            else:
                seen.add(seq)
        return list(ans)
        """
        seen = set()
        ans = []

        for i in range(len(s) - 9):
            x = s[i:i+10]

            if x in seen:
                if x not in ans:
                    ans.append(x)
            else:
                seen.add(x)

        return ans