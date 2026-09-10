class Solution(object):
    def maxProduct(self, words):
        """
        :type words: List[str]
        :rtype: int
        """
        n = len(words)
        m = []
        for i in words:
            ma = 0
            for ch in i:
                ma |= 1 << (ord(ch) - ord('a'))
            m.append(ma)
        ans = 0
        for i in range(n):
            for j in range(i + 1, n):
                if m[i] & m[j] == 0:
                    ans = max(ans, len(words[i]) * len(words[j]))
        return ans