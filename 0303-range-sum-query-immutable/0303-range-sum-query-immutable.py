class NumArray(object):

    def __init__(self, nums):
        """
        :type nums: List[int]
        """
        self.p = [0]
        for x in nums:
            self.p.append(self.p[-1] + x)

    def sumRange(self, left, right):
        """
        :type left: int
        :type right: int
        :rtype: int
        """
        return self.p[right + 1] - self.p[left]

# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)