class Solution(object):
    def combinationSum2(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        candidates.sort()
        ans = []
        def bt(st, curr, tot):
            if tot == target:
                ans.append(curr[:])
                return
            for i in range(st, len(candidates)):
                if tot + candidates[i] > target:
                    break
                if i > st and candidates[i] == candidates[i - 1]:
                    continue
                curr.append(candidates[i])
                bt(i + 1, curr, tot + candidates[i])
                curr.pop()
        bt(0, [], 0)
        return ans