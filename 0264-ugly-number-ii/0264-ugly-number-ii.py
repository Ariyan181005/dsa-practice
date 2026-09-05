class Solution(object):
    def nthUglyNumber(self, n):
        """
        :type n: int
        :rtype: int
        """
        u=[1]
        i2 = i3 = i5 = 0
        for _ in range(1,n):
            n=min(u[i2]*2,u[i3]*3,u[i5]*5)
            u.append(n)
            if n == u[i2]*2:
                i2 += 1
            if n == u[i3]*3:
                i3 += 1
            if n == u[i5]*5:
                i5 += 1
        return u[-1]