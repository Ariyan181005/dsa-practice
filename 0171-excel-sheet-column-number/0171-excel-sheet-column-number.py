class Solution(object):
    def titleToNumber(self, columnTitle):
        """
        :type columnTitle: str
        :rtype: int
        """
        a=0
        for i in columnTitle:
            a= a*26+(ord(i)-65+1)
        return a