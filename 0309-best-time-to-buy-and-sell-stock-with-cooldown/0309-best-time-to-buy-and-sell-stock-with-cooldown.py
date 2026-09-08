class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        h = -prices[0]
        s = 0
        r = 0
        for i in range(1, len(prices)):
            oh = h
            os = s
            ore = r
            h = max(oh, ore - prices[i])
            s = oh + prices[i]
            r = max(ore, os)
        return max(s, r)