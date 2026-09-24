class Solution:
    def smallestIndex(self, nums: List[int]) -> int:
        """
        s=[]
        for i in nums:
            s.append(sum(int(d) for d in str(i)))
        for i in range(len(s)):
            if s[i]==i:
                return i
                break
        else:
            return -1
        """
        for i in  range(len(nums)):
            if sum(map(int, str(nums[i]))) == i:
                return i
        return - 1