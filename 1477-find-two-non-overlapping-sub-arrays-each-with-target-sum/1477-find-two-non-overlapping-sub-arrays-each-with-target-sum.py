class Solution:
    def minSumOfLengths(self, arr: List[int], target: int) -> int:
        n = len(arr)
        mp = {0: -1}
        b = [n + 1] * n
        s = 0
        ans = n + 1
        mn = n + 1
        for i in range(n):
            s += arr[i]
            if s - target in mp:
                j = mp[s - target]
                ln = i - j
                if j >= 0:
                    ans = min(ans, ln + b[j])
                mn = min(mn, ln)
            b[i] = mn
            mp[s] = i
        if ans == n + 1:
            return -1
        return ans