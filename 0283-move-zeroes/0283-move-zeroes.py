class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        """
        for i in nums:
            if i==0:
                nums.append(nums.pop(nums.index(i)))
        """
        inx = 0
        for i in range(len(nums)):
            if nums[i] != 0:
                nums[inx] = nums[i]
                inx += 1
        while inx < len(nums):
            nums[inx] = 0
            inx += 1