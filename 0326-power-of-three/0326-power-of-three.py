class Solution(object):
    def isPowerOfThree(self, n):
        """
        :type n: int
        :rtype: bool
        """
        """
        #easy but time consuming
        if n <= 0:
            return False
        while n>1:
            if n%3==0:
                n=n//3
            else:
                return False
        return True
        """
        #recursive
        if n == 1:
            return True
        if n <= 0 or n % 3 != 0:
            return False
        return self.isPowerOfThree(n // 3)