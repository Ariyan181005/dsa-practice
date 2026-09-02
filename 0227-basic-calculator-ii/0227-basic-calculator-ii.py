class Solution(object):
    def calculate(self, s):
        """
        :type s: str
        :rtype: int
        """
        st = []
        n = 0
        si = '+'
        for i in range(len(s)):
            ch = s[i]
            if ch.isdigit():
                n = n * 10 + int(ch)
            if (not ch.isdigit() and ch != ' ') or i == len(s) - 1:
                if si == '+':
                    st.append(n)
                elif si == '-':
                    st.append(-n)
                elif si == '*':
                    st.append(st.pop() * n)
                elif si == '/':
                    x = st.pop()
                    if x < 0:
                        st.append(-(-x // n))
                    else:
                        st.append(x // n)
                si = ch
                n = 0
        return sum(st)