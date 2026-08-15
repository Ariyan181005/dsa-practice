class Solution(object):
    def myAtoi(self, s):
        s = s.strip()

        if s == "":
            return 0

        sign = 1

        if s[0] == '-':
            sign = -1
            s = s[1:]
        elif s[0] == '+':
            s = s[1:]

        num = 0

        for i in range(len(s)):
            if not s[i].isdigit():
                break

            num = num * 10 + (ord(s[i]) - ord('0'))

        num = num * sign

        if num < -2**31:
            return -2**31

        if num > 2**31 - 1:
            return 2**31 - 1

        return num