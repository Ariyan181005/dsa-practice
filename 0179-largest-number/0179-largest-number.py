class Solution(object):
    def largestNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: str
        """
        """
        nums=[str(x)for x in nums]
        n=len(nums)
        for i in range(n):
            for j in range(i+1,n):
                if nums[i]+nums[j] < nums[j]+nums[i]:
                    nums[i],nums[j]=nums[j],nums[i]
        ans=''.join(nums)
        if ans[0]=='0':
            return '0'
        return ans
        """
        nums = list(map(str, nums))
        nums.sort(key=lambda x: x * 10, reverse=True)
        if nums[0] == "0":
            return "0"
        return ''.join(nums)