class Solution:
    def stoneGameIII(self, stoneValue: List[int]) -> str:
        # cannot treat this as greedy
        # must explore all choices and return the maximum route from this position

        # we actually don't need to have a global variable denoting who wins
        # because to figure out the winner we can have our dp function return the maximum value alice can get since she starts first
        # and see if it's greater or less than half of the total stone sums once we exit our overall function
        
        # at each step, we want to simulate only alice
        # make bob an implicit choice (we skip over him)

        # we only explore alice's steps
        # at each step, we have the option to either take 1, 2, or 3 stones
        # maintain a queue of stones to pop from
        # within each decision that we make, we must extend to 3 options (bob takes 1 2 or 3 stones)
        # this means we need a nested for loop
        # outer is for alice's choices, inner is for bob's choices
        # we actually don't need to maintain a queue we can just move our index 
        # to simulate our queue

        # actually, bob will also play optimally
        # this means that we need to simulate both at the same time
        # at each step, be agnostic to what player we are
        # just do what is optimal from here
        memo = {}
        def dfs(i):
            if i in memo:
                return memo[i]
            if i == len(stoneValue):
                return 0
            if i > len(stoneValue):
                return sys.maxsize
            
            # simulate our choices
            # what if we are adding/subtracting to an overall score?
            # this is the diff between alice and bob
            # we add alice's choice
            # and subtract bob's choice
            # we simulate both at a current stage?

            # do we need to track if we're subtracting or adding to a given score?
            # or can we abstract that out to the call logic?
            # also, how do we make the optimal choice for a given player because opposite players
            # want to go to opposite ends (negative sum or positive sum)

            # let's say at a given stage we want to maximize our options
            # we need to simulate both alice and bob at this moment
            # and then call the recursive function on bob and our next option as alice
            
            maxval = -sys.maxsize
            for j in range(1,4):
                if not i+j <= len(stoneValue):
                    break
                bob = dfs(i+j)
                maxval = max(maxval, sum(stoneValue[i:i+j]) - bob)
            
            memo[i] = maxval
            return maxval
        
        #alice = dfs(0)
        #print(alice)

        # i need to do bottom-up dp
        dp = [0 for _ in range(len(stoneValue)+1)]

        for i in range(len(stoneValue)-1, -1, -1):
            # at this position, we need to compute the highest possible score
            # we have three choices: take 1, 2, or 3
            # and then subtract the optimal for the next decision
            
            # explore our three choices
            optimal = -sys.maxsize
            for j in range(1, 4):
                if i+j > len(stoneValue):
                    break
                curr = sum(stoneValue[i:i+j]) - dp[i+j]
                optimal = max(optimal, curr)
            
            dp[i] = optimal
        alice = dp[0]
        
        if alice > 0:
            return "Alice"
        elif alice < 0:
            return "Bob"
        else:
            return "Tie"
        
        
        

