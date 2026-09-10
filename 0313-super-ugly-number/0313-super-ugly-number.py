class Solution(object):
    def nthSuperUglyNumber(self, n, primes):
        """
        :type n: int
        :type primes: List[int]
        :rtype: int
        """
        u = [1]
        ind = [0] * len(primes)
        for i in range(1, n):
            mn = float('inf')
            for j in range(len(primes)):
                mn = min(mn, primes[j] * u[ind[j]])
            u.append(mn)
            for j in range(len(primes)):
                if primes[j] * u[ind[j]] == mn:
                    ind[j] += 1
        return u[-1]