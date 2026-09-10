class Solution(object):
    def wiggleSort(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        n=len(nums)
        a=sorted(nums)
        mid = (n+1)//2
        j=mid-1
        k=n-1
        for i in range(n):
            if i%2 == 0:
                nums[i] = a[j]
                j-=1
            else:
                nums[i]=a[k]
                k-=1
