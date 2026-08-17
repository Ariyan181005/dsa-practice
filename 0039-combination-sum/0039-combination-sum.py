class Solution(object):
    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        ans = []
        def bt(st, curr, tot):
            if tot == target:
                ans.append(curr[:])
                return
            if tot > target:
                return
            for i in range(st, len(candidates)):
                curr.append(candidates[i])
                bt(i, curr, tot + candidates[i])
                curr.pop()
        bt(0, [], 0)
        return ans