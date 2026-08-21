class Solution(object):
    def grayCode(self, n):
        """
        :type n: int
        :rtype: List[int]
        """
        a=[]
        for i in range(1<<n):
            a.append(i^(i>>1))
        return a