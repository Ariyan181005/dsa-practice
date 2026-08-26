class Solution(object):
    def evalRPN(self, tokens):
        """
        :type tokens: List[str]
        :rtype: int
        """
        st = []
        for i in tokens:
            if i not in ["+", "-", "*", "/"]:
                st.append(int(i))
            else:
                b = st.pop()
                a = st.pop()
                if i == "+":
                    st.append(a + b)
                elif i == "-":
                    st.append(a - b)
                elif i == "*":
                    st.append(a * b)
                else:
                    if a*b<0:
                        st.append(-((-a)//b))
                    else:
                        st.append(a // b)
        return st[-1]