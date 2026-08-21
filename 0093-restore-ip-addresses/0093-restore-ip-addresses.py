class Solution(object):
    def restoreIpAddresses(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        n = len(s)
        res = []
        stack = [(0, [])]
        while stack:
            start, parts = stack.pop()
            if len(parts) == 4:
                if start == n:
                    res.append('.'.join(parts))
                continue
            remaining_slots = 4 - len(parts)
            remaining_chars = n - start
            if remaining_chars < remaining_slots:
                continue
            if remaining_chars > remaining_slots * 3:
                continue
            for length in range(1, 4):
                if start + length > n:
                    break
                seg = s[start:start + length]
                if len(seg) > 1 and seg[0] == '0':
                    continue
                if int(seg) > 255:
                    continue
                stack.append((start + length, parts + [seg]))
        return res