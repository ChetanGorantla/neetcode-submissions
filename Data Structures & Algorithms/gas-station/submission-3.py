class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        # total gas must be greater than total cost?
        totalgas = 0
        totalcost = 0

        for i in range(len(gas)):
            totalgas += gas[i]
            totalcost += cost[i]     
        
        if totalgas < totalcost:
            return -1

        ind = 0
        total = 0
        for i in range(len(gas)):
            total += gas[i] - cost[i]
            if total < 0:
                # this state and all previous states don't work, so move up a position
                total = 0
                ind = i+1
        return ind