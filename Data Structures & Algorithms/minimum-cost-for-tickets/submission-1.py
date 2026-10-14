class Solution:
    def mincostTickets(self, days: List[int], costs: List[int]) -> int:
        # min cost to cover alll days
        # do this bottom-up?
        # at each day, we need to figure out the mincost to access this day
        # at the earlier days we need to choose an option that covers a
        # certain range
        # set a end date
        # on our next recursive call, for the next day, check to see if end date >= curr date. if it does, we don't need to add to pathcost
        # if end date < curr date, then we need to buy a new ticket, so
        # explore all options and branch off from there

        memo = {}
        def dfs(i, end):
            if i == len(days):
                return 0
            if (i,end) in memo:
                return memo[(i,end)]
            # we're not at the end, we need to continue searching
            # take a look at end
            mincost = sys.maxsize
            if end >= days[i]:
                # we can extend the existing cost
                mincost = min(mincost, dfs(i+1, end))
            else:
                # we need to explore our candidate options
                for j in range(len(costs)):
                    cost = costs[j]
                    if j == 0:
                        day = 1
                    elif j == 1:
                        day = 7
                    else:
                        day = 30
                    mincost = min(mincost, cost + dfs(i+1, days[i] + day-1))

            memo[(i,end)] = mincost
            return mincost
        return dfs(0,0)