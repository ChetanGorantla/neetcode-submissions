class Solution:
    def stoneGame(self, piles: List[int]) -> bool:
        # return a result if we choose optimally
        # this stage - next option
        # remain agnostic of your current player, just choose optimal approach
        # and subtract the opponent
        # maintain our l and r pointers
        # to see where we are at in our step
        # we can choose whichever one we want and backtrack as such
        memo = {}
        def best(l, r):
            # base case is that we've finished looking for everything
            if l > r:
                return 0
            
            if (l,r) in memo:
                return memo[(l, r)]

            # we haven't finished taking all piles.
            # explore our options
            # we can either take from start or take from end
            result = max(piles[l] - best(l+1, r), piles[r] - best(l, r-1))
            memo[(l,r)] = result
            return result
        
        alice_score = best(0, len(piles)-1)

        if alice_score >= 0:
            return True
        
        return False
