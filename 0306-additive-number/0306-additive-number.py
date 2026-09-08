class Solution(object):
    def isAdditiveNumber(self, num):
        """
        :type num: str
        :rtype: bool
        """
        n = len(num)
        def check(a, b, start):
            while start < n:
                c = a + b
                s = str(c)
                if num[start:start + len(s)] != s:
                    return False
                start += len(s)
                a, b = b, c
            return True
        for i in range(1, n):
            if num[0] == '0' and i > 1:
                break
            a = int(num[:i])
            for j in range(i + 1, n):
                if num[i] == '0' and j - i > 1:
                    break
                b = int(num[i:j])
                if check(a, b, j):
                    return True
        return False