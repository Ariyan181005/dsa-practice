class Solution(object):
    def removeDuplicateLetters(self, s):
        """
        :type s: str
        :rtype: str
        """
        st = []
        se = set()
        lt = {}
        for i in range(len(s)):
            lt[s[i]] = i
        for i in range(len(s)):
            ch = s[i]
            if ch in se:
                continue
            while st and st[-1] > ch and lt[st[-1]] > i:
                se.remove(st.pop())
            st.append(ch)
            se.add(ch)
        return ''.join(st)