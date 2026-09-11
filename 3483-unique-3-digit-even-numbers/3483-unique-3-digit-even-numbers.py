class Solution(object):
    def totalNumbers(self, digits):
        """
        :type digits: List[int]
        :rtype: int
        """
        ans = set()
        for i in range(1, 10):
            for j in range(10):
                for k in range(0, 10, 2):
                    if i in digits and j in digits and k in digits:
                        a = digits[:]
                        a.remove(i)
                        if j in a:
                            a.remove(j)
                        else:
                            continue
                        if k in a:
                            a.remove(k)
                        else:
                            continue
                        num = i * 100 + j * 10 + k
                        ans.add(num)
        return len(ans)