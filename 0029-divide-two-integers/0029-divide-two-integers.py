class Solution(object):
    def divide(self, dividend, divisor):
        """
        :type dividend: int
        :type divisor: int
        :rtype: int
        """
        s=1
        if dividend < 0:
            s=-s
            dividend=-dividend
        if divisor < 0:
            s=-s
            divisor=-divisor
        c=0
        while dividend>=divisor:
            temp=divisor
            count=1
            while dividend >= temp+temp:
                temp+=temp
                count+=count
            dividend-=temp
            c+=count
        if s<0:
            c=-c
        if c > 2147483647:
            return 2147483647
        return c