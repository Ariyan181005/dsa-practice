class Solution(object):
    def reverseDegree(self, s):
        """
        :type s: str
        :rtype: int
        """
        ans, idx = 0, 1
        for ch in s:
            ans+= (123 - ord(ch)) * idx
            idx+= 1
        return ans   