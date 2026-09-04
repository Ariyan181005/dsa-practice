class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        d = {}
        for x in s:
            d[x] = d.get(x, 0) + 1
        for x in t:
            if x not in d:
                return False
            d[x] -= 1
            if d[x] < 0:
                return False
        return True