class Solution:
    def numberOfSets(self, n: int, k: int) -> int:
        """
        mod = 1000000007
        r = 2 * k
        ans = 1
        for i in range(1, r + 1):
            ans = ans * (n + k - i) % mod
            ans = ans * pow(i, mod - 2, mod) % mod
        return ans
        """
        return math.comb(n+k-1,2*k)%(10**9+7)