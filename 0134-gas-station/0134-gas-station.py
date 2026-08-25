class Solution(object):
    def canCompleteCircuit(self, gas, cost):
        """
        :type gas: List[int]
        :type cost: List[int]
        :rtype: int
        """
        if sum(gas)<sum(cost):
            return -1
        t=0
        s=0
        for i in range(len(gas)):
            t+=gas[i]-cost[i]
            if t<0:
                s=i+1
                t=0
        return s