from collections import deque
class Solution(object):
    def findMinHeightTrees(self, n, edges):
        """
        :type n: int
        :type edges: List[List[int]]
        :rtype: List[int]
        """
        if n == 1:
            return [0]
        g = [[] for _ in range(n)]
        deg = [0] * n
        for u, v in edges:
            g[u].append(v)
            g[v].append(u)
            deg[u] += 1
            deg[v] += 1
        q = deque()
        for i in range(n):
            if deg[i] == 1:
                q.append(i)
        rem = n
        while rem > 2:
            size = len(q)
            rem -= size
            for _ in range(size):
                u = q.popleft()
                for v in g[u]:
                    deg[v] -= 1
                    if deg[v] == 1:
                        q.append(v)
        return list(q)