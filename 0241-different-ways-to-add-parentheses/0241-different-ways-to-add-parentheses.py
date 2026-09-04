class Solution:
    def diffWaysToCompute(self, expression: str) -> List[int]:
        memo = {}
        def dp(ex):
            ret = []
            if ex in memo:
                return memo[ex]
            if ex.isdigit():
                return [int(ex)]
            for i, c in enumerate(ex):
                if c.isdigit():
                    continue
                lt = dp(ex[:i])
                rt = dp(ex[i+1:])
                for l in lt:
                    for r in rt:
                        if c == '+':
                            ret.append(l + r)
                        elif c == '-':
                            ret.append(l-r)
                        elif c == '*':
                            ret.append(l*r)
            return ret
        return dp(expression)