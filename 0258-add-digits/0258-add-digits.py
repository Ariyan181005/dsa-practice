class Solution(object):
    def addDigits(self, num):
        """
        :type num: int
        :rtype: int
        """
        """
        while num >= 10:
            num = sum(int(i) for i in str(num))
        return num
        """
        if num == 0:
            return 0
        return 1 + (num - 1) % 9