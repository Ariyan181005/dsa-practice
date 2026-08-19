class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        if digits[-1]<9:
            digits[-1]+=1
            return digits
        digits.pop()
        if len(digits) == 0:
            return [1, 0]
        digits = self.plusOne(digits)
        digits.extend([0])
        return digits