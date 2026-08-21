class Solution(object):
    def restoreIpAddresses(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        res = []
        def bt(index, parts):
            if len(parts) == 4:
                if index == len(s):
                    res.append(".".join(parts))
                return
            remaining = len(s) - index
            slots = 4 - len(parts)
            if remaining < slots or remaining > slots * 3:
                return
            for length in range(1, 4):
                if index + length > len(s):
                    break
                part = s[index:index + length]
                if len(part) > 1 and part[0] == '0':
                    break
                if int(part) > 255:
                    break
                parts.append(part)
                bt(index + length, parts)
                parts.pop()
        bt(0, [])
        return res