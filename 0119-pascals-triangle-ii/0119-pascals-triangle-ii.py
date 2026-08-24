class Solution(object):
    def getRow(self, rowIndex):
        """
        :type rowIndex: int
        :rtype: List[int]
        """
        """
        r=[1]
        for i in range(rowIndex):
            new_r=[1]
            for j in range(1,len(r)):
                new_r.append(r[j-1]+r[j])
            new_r.append(1)
            r=new_r
        return r
        """
        a,b=[],[]
        for i in range(rowIndex+1):
            a=[]
            for j in range(i+1):
                if j==0 or j==i:
                    a+=[1]
                else:
                    a+=[b[j-1]+b[j]]
            b=a
        return a