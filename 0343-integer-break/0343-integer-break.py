class Solution:
    def integerBreak(self, n: int) -> int:
        if n==2:
            return 1
        if n==3:
            return 2
        a=n//3
        if(n-(a*3)==1):
            a=a-1
            return (3**a)*4
        return (3**a)*(n-(a*3)) if n%3!=0 else 3**a