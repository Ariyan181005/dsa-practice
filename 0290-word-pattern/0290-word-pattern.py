class Solution(object):
    def wordPattern(self, pattern, s):
        """
        :type pattern: str
        :type s: str
        :rtype: bool
        """
        words = s.split()
        if len(pattern) != len(words):
            return False
        p = {}
        w = {}
        for i in range(len(pattern)):
            a = pattern[i]
            b = words[i]
            if a in p and p[a] != b:
                return False
            if b in w and w[b] != a:
                return False
            p[a] = b
            w[b] = a
        return True