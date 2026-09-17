class Solution:
    def minSumOfLengths(self, arr: List[int], target: int) -> int:
        n, ans, tot = len(arr), len(arr) + 1, 0
        dp = [n] * (n + 1)
        lt = 0
        for rt in range(len(arr)):
            tot+=arr[rt]
            while tot>target:
                tot-=arr[lt]
                lt+=1
            dp[rt+1]=dp[rt]
            if tot==target:
                ans=min(ans,rt-lt+1+dp[lt])
                dp[rt+1]=min(dp[rt],rt-lt+1)
        return -1 if ans==n+1 else ans