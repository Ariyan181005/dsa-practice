class Solution(object):
    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        """
        if x < 2:
            return x
        lt = 1
        rt = x
        ans = 0
        while lt <= rt:
            mid = (lt + rt) // 2
            if mid * mid == x:
                return mid
            elif mid * mid < x:
                ans = mid
                lt = mid + 1
            else:
                rt = mid - 1
        return ans