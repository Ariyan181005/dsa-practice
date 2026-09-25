class Solution:
    def braceExpansionII(self, expression: str) -> list[str]:
        def dfs(s):
            ans = set()
            i = 0
            while i < len(s):
                if s[i] == '{':
                    cnt = 1
                    j = i + 1
                    while cnt:
                        if s[j] == '{':
                            cnt += 1
                        elif s[j] == '}':
                            cnt -= 1
                        j += 1
                    inside = dfs(s[i + 1:j - 1])
                    if not ans:
                        ans = inside
                    else:
                        ans = {a + b for a in ans for b in inside}
                    i = j
                elif s[i] == ',':
                    rest = dfs(s[i + 1:])
                    if not ans:
                        ans = rest
                    else:
                        ans |= rest
                    break
                else:
                    j = i
                    while j < len(s) and s[j].islower():
                        j += 1
                    word = s[i:j]
                    if not ans:
                        ans = {word}
                    else:
                        ans = {a + word for a in ans}
                    i = j
            return ans
        return sorted(dfs(expression))