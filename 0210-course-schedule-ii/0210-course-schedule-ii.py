class Solution(object):
    def findOrder(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: List[int]
        """
        g = [[] for _ in range(numCourses)]
        i = [0] * numCourses
        for a, b in prerequisites:
            g[b].append(a)
            i[a] += 1
        q = deque()
        for io in range(numCourses):
            if i[io] == 0:
                q.append(io)
        ans = []
        while q:
            c = q.popleft()
            ans.append(c)
            for nxt in g[c]:
                i[nxt] -= 1
                if i[nxt] == 0:
                    q.append(nxt)
        if len(ans) == numCourses:
            return ans
        return []