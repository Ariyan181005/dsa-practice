class Solution(object):
    def stoneGameV(self, stoneValue):
        n = len(stoneValue)
        prefix = [0] * (n + 1)
        for i in range(n):
            prefix[i + 1] = prefix[i] + stoneValue[i]
        memo = {}
        def dfs(i, j):
            if i >= j:
                return 0
            if (i, j) in memo:
                return memo[(i, j)]
            answer = 0
            left_sum = 0
            right_sum = prefix[j + 1] - prefix[i]
            for k in range(i, j):
                left_sum += stoneValue[k]
                right_sum -= stoneValue[k]
                if left_sum < right_sum:
                    if answer >= left_sum * 2:
                        continue
                    answer = max(answer,left_sum + dfs(i, k))
                elif left_sum > right_sum:
                    if answer >= right_sum * 2:
                        break
                    answer = max(answer,right_sum + dfs(k + 1, j))
                else:
                    answer = max(answer,left_sum + dfs(i, k),right_sum + dfs(k + 1, j))
            memo[(i, j)] = answer
            return answer
        return dfs(0, n - 1)