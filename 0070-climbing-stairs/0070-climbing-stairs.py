class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n <= 2:
            return n
        a = 1
        b = 1
        for i in range(n):
            c = a + b
            a = b
            b = c
        return a