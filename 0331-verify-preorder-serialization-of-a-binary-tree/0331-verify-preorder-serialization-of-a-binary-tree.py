class Solution(object):
    def isValidSerialization(self, preorder):
        """
        :type preorder: str
        :rtype: bool
        """
        sl = 1
        for i in preorder.split(','):
            if sl == 0:
                return False
            if i == '#':
                sl -= 1
            else:
                sl += 1
        return sl == 0