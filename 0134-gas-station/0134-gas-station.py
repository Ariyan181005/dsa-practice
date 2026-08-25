class Solution(object):
    def canCompleteCircuit(self, gas, cost):
        """
        :type gas: List[int]
        :type cost: List[int]
        :rtype: int
        """
        tot=0
        tank=0
        st=0
        for i in range(len(gas)):
            tank+=gas[i]-cost[i]
            tot+=gas[i]-cost[i]
            if tank<0:
                st=i+1
                tank=0
        if tot>=0:
            return st
        else:
            return -1