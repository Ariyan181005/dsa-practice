class Solution(object):
    def partition(self, s):
        """
        :type s: str
        :rtype: List[List[str]]
        """
        op = []
        def backtrack(st, path):
            if st == len(s):
                op.append(path[:])
                return
            for i in range(st, len(s)):
                x = s[st:i+1]
                if x == x[::-1]:
                    path.append(x)
                    backtrack(i + 1, path)
                    path.pop()
        backtrack(0, [])
        return op