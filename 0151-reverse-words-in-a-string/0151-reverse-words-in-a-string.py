class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        s=" ".join(s.split())
        s=s.split()
        a=" ".join(s[::-1])
        return a