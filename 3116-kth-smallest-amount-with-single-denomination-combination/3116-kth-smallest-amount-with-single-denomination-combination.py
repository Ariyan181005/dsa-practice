class Solution(object):
    def findKthSmallest(self, coins, k):
        """
        :type coins: List[int]
        :type k: int
        :rtype: int
        """
        def gcd(a,b):
            while b:
                a,b=b,a%b
            return a
        n = len(coins)
        def lcm(a, b):
            return a // gcd(a, b) * b
        def count(x):
            total = 0
            for mask in range(1, 1 << n):
                curr_lcm = 1
                bits = 0
                for i in range(n):
                    if mask & (1 << i):
                        bits += 1
                        curr_lcm = lcm(curr_lcm, coins[i])
                        if curr_lcm > x:
                            break
                else:
                    multiples = x // curr_lcm
                    if bits % 2 == 1:
                        total += multiples
                    else:
                        total -= multiples
            return total
        left = 1
        right = min(coins) * k
        while left < right:
            mid = (left + right) // 2
            if count(mid)>=k:
                right=mid
            else:
                left=mid+1
        return left