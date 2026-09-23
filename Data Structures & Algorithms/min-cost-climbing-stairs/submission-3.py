class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        # at each step, determine which cost of 
        # 1 or 2 was cheaper
        #
        l = cost[0]
        r = cost[1]
        # define a state as "min cost of getting past this step"

        for i in range(2, len(cost)):
            # we can either consider l + curr
            # or just r
            curr = min(l, r) + cost[i]
            #print(i, curr)
            l = r
            r = curr
        
        return min(l, r)

        # 1 2 1 2 1 1 1
        # 1 2 2 4 3 4 4
