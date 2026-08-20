class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) <= 2:
            return len(nums)
        w = 2
        for i in range(2, len(nums)):
            if nums[i] != nums[w - 2]:
                nums[w] = nums[i]
                w += 1
        return w