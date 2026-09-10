class Solution(object):
    def maxProduct(self, words):
        """
        :type words: List[str]
        :rtype: int
        """
        m = {}
        for word in words:
            mask = 0
            for char in word:
                mask |= 1 << (ord(char) - ord('a'))
            m[mask] = max(m.get(mask, 0), len(word)) 
        max_prod = 0
        for mask1, len1 in m.items():
            for mask2, len2 in m.items():
                if (mask1 & mask2) == 0:
                    max_prod = max(max_prod, len1 * len2) 
        return max_prod