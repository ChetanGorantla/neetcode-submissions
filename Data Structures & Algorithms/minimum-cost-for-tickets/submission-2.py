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

        # instead of tracking end, when we make a decision, just jump
        # straight to the first day that we don't cover
        memo = {}
        def dfs(i):
            if i == len(days):
                return 0
            if i in memo:
                return memo[i]
            # we're not at the end, we need to continue searching
            # take a look at end
            mincost = sys.maxsize
            
            # we need to explore our candidate options
            for j in range(len(costs)):
                new_i = i
                cost = costs[j]
                if j == 0:
                    day = 1
                elif j == 1:
                    day = 7
                else:
                    day = 30
                # find the index based on this days[i]+day-1
                end_day = days[i]+day-1
                while new_i+1 < len(days) and days[new_i+1] <= end_day:
                    new_i+=1
                mincost = min(mincost, cost + dfs(new_i+1))

            memo[i] = mincost
            return mincost
        return dfs(0)