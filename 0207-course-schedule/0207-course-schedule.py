class Solution(object):
    def canFinish(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: bool
        """
        g = [[] for _ in range(numCourses)]
        for a, b in prerequisites:
            g[b].append(a)
        s = [0] * numCourses
        def dfs(c):
            if s[c] == 1:
                return False
            if s[c] == 2:
                return True
            s[c] = 1
            for nxt in g[c]:
                if not dfs(nxt):
                    return False
            s[c] = 2
            return True
        for i in range(numCourses):
            if not dfs(i):
                return False
        return True