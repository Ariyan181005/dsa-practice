class Solution(object):
    def threeSumClosest(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        nums.sort()
        c =nums[0] + nums[1] + nums[2]
        for i in range(len(nums)-2):
            l,r=i+1,len(nums)-1
            while l<r:
                total=nums[i]+nums[l]+nums[r]
                if abs(total-target)<abs(c-target):
                    c =total
                if total<target:
                    l+=1
                elif total>target:
                    r-=1
                else:
                    return total
        return c