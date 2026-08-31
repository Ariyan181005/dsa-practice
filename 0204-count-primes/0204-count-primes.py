class Solution(object):
    def countPrimes(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n <= 2:
            return 0
        p = [True] * n
        p[0] = p[1] = False
        for i in range(2, int(n ** 0.5) + 1):
            if p[i]:
                p[i * i:n:i] = [False] * (((n - 1 - i * i) // i) + 1)
        return sum(p)