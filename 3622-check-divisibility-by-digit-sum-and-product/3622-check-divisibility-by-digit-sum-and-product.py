class Solution(object):
    def checkDivisibility(self, n):
        """
        :type n: int
        :rtype: bool
        """
        s=str(n)
        s=list(s)
        sumation=0
        product=1
        for i in s:
            sumation+=int(i)
            product*=int(i)
        fin=sumation+product
        if n%fin==0:
            return True
        else:
            return False