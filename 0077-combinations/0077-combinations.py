class Solution(object):
    def combine(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: List[List[int]]
        """
        r = []
        def bt(st, cur):
            if len(cur) == k:
                r.append(cur[:])
                return
            for i in range(st, n + 1):
                cur.append(i)
                bt(i + 1, cur)
                cur.pop()
        bt(1, [])
        return r