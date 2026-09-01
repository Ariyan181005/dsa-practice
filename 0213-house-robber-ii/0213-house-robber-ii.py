class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums)==1:
            return nums[0]
        def sol(a):
            prev=0
            cur=0
            for i in a:
                n = max(cur,prev+i)
                prev,cur=cur,n
            return cur
        return max(sol(nums[1:]),sol(nums[:-1]))