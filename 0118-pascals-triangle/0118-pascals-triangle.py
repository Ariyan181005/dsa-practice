class Solution(object):
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        l=[]
        for i in range(numRows):
            r=[1]*(i+1)
            for j in range(1,i):
                r[j]=l[i-1][j-1]+l[i-1][j]
            l.append(r)
        return l