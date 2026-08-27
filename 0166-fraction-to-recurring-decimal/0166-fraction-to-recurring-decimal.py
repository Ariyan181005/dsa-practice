class Solution(object):
    def fractionToDecimal(self, numerator, denominator):
        """
        :type numerator: int
        :type denominator: int
        :rtype: str
        """
        if numerator == 0:
            return "0"
        sign = ""
        if (numerator < 0) != (denominator < 0):
            sign = "-"
        numerator = abs(numerator)
        denominator = abs(denominator)
        ans = sign + str(numerator // denominator)
        rem = numerator % denominator
        if rem == 0:
            return ans
        ans += "."
        seen = {}
        while rem != 0:
            if rem in seen:
                pos = seen[rem]
                ans = ans[:pos] + "(" + ans[pos:] + ")"
                return ans
            seen[rem] = len(ans)
            rem *= 10
            ans += str(rem // denominator)
            rem %= denominator
        return ans