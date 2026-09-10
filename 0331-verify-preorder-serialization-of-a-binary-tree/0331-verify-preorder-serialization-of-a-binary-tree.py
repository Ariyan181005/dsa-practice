class Solution(object):
    def isValidSerialization(self, preorder):
        """
        :type preorder: str
        :rtype: bool
        """
        a=preorder.split(",")
        sl=1
        for i in a:
            sl -=1
            if sl < 0:
                return False
            if i != "#":
                sl += 2
        return sl == 0