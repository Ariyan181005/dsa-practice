class Solution:
    def trap(self, height: list[int]) -> int:
        if not height:
            return 0
        n = len(height)
        lmax = [0] * n
        rmax = [0] * n
        mini = [0] * n
        ans = [0] * n
        lmax[0] = height[0]
        rmax[n-1] = height[n-1]
        for i in range(1, n):
            lmax[i] = max(height[i], lmax[i-1])
        for i in range(n-2, -1, -1):
            rmax[i] = max(height[i], rmax[i+1])
        for i in range(n):
            mini[i] = min(lmax[i], rmax[i])
        for i in range(n):
            sub = mini[i] - height[i]
            if sub > 0:
                ans[i] = sub
        return sum(ans)