class Solution(object):
    def myPow(self, x, n):
        """
        :type x: float
        :type n: int
        :rtype: float
        """
        """
        p=1
        if n>0:
            while n>0:
                p*=x
                n-=1
        else:
            while n<0:
                p/=x
                n+=1
        return p
        """
        if n < 0:
            x = 1 / x
            n = -n
        p = 1
        while n > 0:
            if n % 2 == 1:
                p *= x
            x *= x
            n //= 2
        return p