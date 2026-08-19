class Solution(object):
    def generateMatrix(self, n):
        """
        :type n: int
        :rtype: List[List[int]]
        """
        mat=[[0]*n for _ in range(n)]
        l,r=0,n-1
        t,b=0,n-1
        val=1
        while l<=r:
            for col in range (l,r+1):
                mat[t][col]=val
                val+=1
            t+=1
            for row in range(t,b+1):
                mat[row][r]=val
                val+=1
            r-=1
            for col in range(r,l-1,-1):
                mat[b][col]=val
                val+=1
            b-=1    
            for row in range(b,t-1,-1):
                mat[row][l]=val
                val+=1
            l+=1
        return mat