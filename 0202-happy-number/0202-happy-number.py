class Solution(object):
    def isHappy(self, n):
        """
        :type n: int
        :rtype: bool
        """
        """
        s=set()
        while n!=1:
            if n in s:
                return False
            s.add(n)
            su=0
            while n>0:
                d= n%10
                su+=d*d
                n//=10
            n=su
        return True
        """
        while(1):
            c=0
            for i in str(n):
                c+=int(i)**2
                n=c
            if(n==4):return False
            if(n==1):return True