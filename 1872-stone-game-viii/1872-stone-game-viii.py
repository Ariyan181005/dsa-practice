class Solution(object):
    def stoneGameVIII(self, stones):
        """
        :type stones: List[int]
        :rtype: int
        """
        n=len(stones)
        for i in range(1,n):
            stones[i]+=stones[i-1]
        a=stones[n-1]
        for i in range(n-2,0,-1):
            a=max(a,stones[i]-a)
        return a 