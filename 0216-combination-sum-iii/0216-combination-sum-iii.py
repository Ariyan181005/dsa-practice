class Solution(object):
    def combinationSum3(self, k, n):
        """
        :type k: int
        :type n: int
        :rtype: List[List[int]]
        """
        a=[]
        def dfs (st,pt,tot):
            if len(pt) == k:
                if tot == n:
                    a.append(pt[:])
                return
            if tot > n:
                return
            for i in range(st,10):
                if tot+i > n :
                    break
                pt.append(i)
                dfs(i+1,pt,tot+i)
                pt.pop()
        dfs(1,[],0)
        return a