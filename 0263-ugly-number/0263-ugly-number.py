class Solution(object):
    def isUgly(self, n):
        """
        :type n: int
        :rtype: bool
        """
        if n<= 0 :
            return False
        for fac in [2,3,5]:
            while n % fac==0:
                n//=fac
        return n == 1