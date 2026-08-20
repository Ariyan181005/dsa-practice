class Solution(object):
    def resultArray(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        arr1=[nums[0]]
        arr2=[nums[1]]
        pt=2
        while pt<len(nums):
            if arr1[-1]<arr2[-1]:
                arr2.append(nums[pt])
            else:
                arr1.append(nums[pt])
            pt+=1
        arr1.extend(arr2)
        return arr1