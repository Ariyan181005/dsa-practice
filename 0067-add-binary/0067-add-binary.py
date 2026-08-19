class Solution(object):
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        bsum = bin(int(a, 2) + int(b, 2))[2:]
        return bsum