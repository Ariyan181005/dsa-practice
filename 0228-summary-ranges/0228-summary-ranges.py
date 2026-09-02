class Solution(object):
    def summaryRanges(self, nums):
        """
        :type nums: List[int]
        :rtype: List[str]
        """
        ans = []
        if not nums:
            return ans
        st = nums[0]
        for i in range(1, len(nums)):
            if nums[i] != nums[i - 1] + 1:
                if st == nums[i - 1]:
                    ans.append(str(st))
                else:
                    ans.append(str(st) + "->" + str(nums[i - 1]))
                st = nums[i]
        if st == nums[-1]:
            ans.append(str(st))
        else:
            ans.append(str(st) + "->" + str(nums[-1]))
        return ans