class Solution(object):
    def stoneGameIX(self, stones):
        """
        :type stones: List[int]
        :rtype: bool
        """
        c = [0, 0, 0]
        for x in stones:
            c[x % 3] += 1

        if c[0] % 2 == 0:
            return c[1] > 0 and c[2] > 0
        else:
            return abs(c[1] - c[2]) > 2
