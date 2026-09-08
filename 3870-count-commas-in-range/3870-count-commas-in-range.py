class Solution(object):
    def countCommas(self, n):
        """
        :type n: int
        :rtype: int
        """
        a=0
        p=1000
        c=1
        while p <= n:
            a+= n-p+1
            p*=1000
            c+=1
        return a