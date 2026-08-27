class Solution(object):
    def lexGreaterPermutation(self, s, target):
        """
        :type s: str
        :type target: str
        :rtype: str
        """
        cnt = [0] * 26
        for i in range(len(s)):
            cnt[ord(s[i]) - ord('a')] += 1
            cnt[ord(target[i]) - ord('a')] -= 1
        t = list(target)
        for i in range(len(s) - 1, -1, -1):
            b = ord(t[i]) - ord('a')
            cnt[b] += 1
            if min(cnt) < 0:
                continue
            for j in range(b + 1, 26):
                if cnt[j] > 0:
                    cnt[j] -= 1
                    t[i] = chr(ord('a') + j)
                    return "".join(t[:i + 1]) + self.getMinString(cnt)
        return ""
    def getMinString(self, cnt):
        res = []
        for i in range(26):
            res.extend([chr(i + ord('a'))] * cnt[i])
        return "".join(res)