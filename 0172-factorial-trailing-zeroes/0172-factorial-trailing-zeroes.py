class Solution(object):
    def trailingZeroes(self, n):
        """
        :type n: int
        :rtype: int
        """
        """
        def fact(a):
            if a==0 or a==1:
                return 1
            return a*fact(a-1)
        f=str(fact(n))
        c=0
        for i in range(len(f)-1,-1,-1):
            if f[i]=="0":
                c+=1
            else:
                break
        return c
        """
        count=0
        while n>0:
            n=n//5
            count=count+n
        return count