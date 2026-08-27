class Solution:
    def lastStoneWeightII(self, stones: List[int]) -> int:
        # problem wants us to find two subsets with a sum as close as possible to
        # the halfway point
        # and find the diff between half and that value
        # if we exceed then that's a failed case

        # at each step, we need to decide whether or not we want to include
        # this stone weight in our subset
        # we need to track the current index we're looking at and the current subset
        # sum. instead of maintaining a sum, we can just maintain a track
        # and see how close to 0 that track can get without getting below it

        stonesum = sum(stones)
        half = (stonesum+1)//2
        memo = {}
        def dfs(i, fill):
            # if we've reached a possible answer or if we reached the end
            # return our answer
            if fill >= half or i == len(stones):
                return abs(fill-(stonesum-fill))

            # we've already hit this
            if (i,fill) in memo:
                return memo[(i,fill)]
            
            # we haven't seen this. explore inclusion exclusion
            ans = min(dfs(i+1, fill), dfs(i+1, fill+stones[i]))
            memo[(i,fill)] = ans
            return ans
        
        return dfs(0, 0)
            

            

