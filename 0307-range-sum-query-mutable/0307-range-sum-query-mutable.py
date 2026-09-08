class NumArray(object):
    def __init__(self, nums):
        """
        :type nums: List[int]
        """
        self.n = len(nums)
        self.tree = [0] * (2 * self.n)
        for i in range(self.n):
            self.tree[self.n + i] = nums[i]
        for i in range(self.n - 1, 0, -1):
            self.tree[i] = self.tree[2 * i] + self.tree[2 * i + 1]

    def update(self, index, val):
        """
        :type index: int
        :type val: int
        :rtype: None
        """
        i = self.n + index
        self.tree[i] = val
        i //= 2
        while i:
            self.tree[i] = self.tree[2 * i] + self.tree[2 * i + 1]
            i //= 2

    def sumRange(self, left, right):
        """
        :type left: int
        :type right: int
        :rtype: int
        """
        left += self.n
        right += self.n
        ans = 0
        while left <= right:
            if left % 2 == 1:
                ans += self.tree[left]
                left += 1
            if right % 2 == 0:
                ans += self.tree[right]
                right -= 1
            left //= 2
            right //= 2
        return ans


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# obj.update(index,val)
# param_2 = obj.sumRange(left,right)