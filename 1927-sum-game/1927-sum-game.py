class Solution(object):
    def sumGame(self, num):
        """
        :type num: str
        :rtype: bool
        """
        n = len(num)
        cnt1 = num[: n // 2].count("?")
        cnt2 = num[n // 2 :].count("?")
        s1 = sum(int(x) for x in num[: n // 2] if x != "?")
        s2 = sum(int(x) for x in num[n // 2 :] if x != "?")
        return (cnt1 + cnt2) % 2 == 1 or s1 - s2 != 9 * (cnt2 - cnt1) // 2