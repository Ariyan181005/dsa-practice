class Solution(object):
    def reverse(self, x):
        if x<0:
            x=str(x)
            a=x[:0:-1]
            a=0-int(a)
        else:
            x=str(x)
            a=x[::-1]
            a=int(a) 
        if a < -2**31 or a > 2**31 - 1:
            return 0
        return a