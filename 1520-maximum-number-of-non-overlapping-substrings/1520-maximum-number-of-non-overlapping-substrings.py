class Solution:
    def maxNumOfSubstrings(self, s: str) -> list[str]:
        ft = {}
        lt = {}
        for i in range(len(s)):
            if s[i] not in ft:
                ft[s[i]] = i
            lt[s[i]] = i
        arr = []
        for c in ft:
            l = ft[c]
            r = lt[c]
            ok = True
            i = l
            while i <= r:
                x = s[i]
                if ft[x] < l:
                    ok = False
                    break
                r = max(r, lt[x])
                i += 1
            if ok:
                arr.append((l, r))
        arr.sort(key=lambda x: x[1])
        ans = []
        end = -1
        for l, r in arr:
            if l > end:
                ans.append(s[l:r+1])
                end = r
        return ans