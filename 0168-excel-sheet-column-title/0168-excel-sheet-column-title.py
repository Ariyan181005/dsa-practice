class Solution(object):
    def convertToTitle(self, columnNumber):
        """
        :type columnNumber: int
        :rtype: str
        """
        a=""
        while columnNumber>0:
            columnNumber-=1
            r=columnNumber%26
            a=chr(r+65)+a
            columnNumber//=26
        return a