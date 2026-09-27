class Solution:
    def reverseParentheses(self, s: str) -> str:
        st = []
        for ch in s:
            if ch == ')':
                temp = []

                while st[-1] != '(':
                    temp.append(st.pop())
                st.pop()

                st.extend(temp)
            else:
                st.append(ch)
        return ''.join(st)