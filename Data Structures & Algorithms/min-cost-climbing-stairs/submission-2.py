class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        one = 0
        two = cost[0]
        if len(cost) == 1:
            return cost[0]
        if len(cost) == 2:
            return cost[1]

        for i in range(2, len(cost)):
            # find the minimum cost to get to the i'th step
            mincost = min(cost[i-1], cost[i-2])
            cost[i]+=mincost
        print(cost)
        return min(cost[-2], cost[-1])