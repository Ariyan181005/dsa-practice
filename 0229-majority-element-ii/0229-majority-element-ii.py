class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        """
        c1 = c2 = None
        n1 = n2 = 0
        for x in nums:
            if x == c1:
                n1 += 1
            elif x == c2:
                n2 += 1
            elif n1 == 0:
                c1 = x
                n1 = 1
            elif n2 == 0:
                c2 = x
                n2 = 1
            else:
                n1 -= 1
                n2 -= 1
        n1 = n2 = 0
        for x in nums:
            if x == c1:
                n1 += 1
            elif x == c2:
                n2 += 1
        ans = []
        if n1 > len(nums) // 3:
            ans.append(c1)
        if n2 > len(nums) // 3:
            ans.append(c2)
        return ans
        """
        n=len(nums)
        fm={}
        res=[]
        for i in nums:
            if i not in fm:
                fm[i]=1
            else:
                fm[i]+=1
        for j in fm:
            if fm[j]>n/3:
                res.append(j)
        return res