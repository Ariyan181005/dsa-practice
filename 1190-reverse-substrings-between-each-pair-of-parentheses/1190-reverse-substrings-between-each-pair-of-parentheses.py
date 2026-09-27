class Solution:
    def reverseParentheses(self, s: str) -> str:
        while '(' in s:
            end=s.find(')')
            start=s.rfind('(',0,end)
            rev_substri=s[start+1:end][::-1]
            s=s[:start]+rev_substri+s[end+1:]
        return s