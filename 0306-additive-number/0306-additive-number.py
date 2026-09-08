class Solution(object):
    def isAdditiveNumber(self, num):
        """
        :type num: str
        :rtype: bool
        """
        n = len(num)
        for i in range(1, n):
            for j in range(i + 1, n):
                a = num[:i]
                b = num[i:j]
                if len(a) > 1 and a[0] == '0':
                    continue
                if len(b) > 1 and b[0] == '0':
                    continue
                x = int(a)
                y = int(b)
                k = j
                count = 2
                while k < n:
                    z = x + y
                    s = str(z)
                    if num[k:k + len(s)] != s:
                        break
                    k += len(s)
                    x = y
                    y = z
                    count += 1
                if k == n and count >= 3:
                    return True
        return False