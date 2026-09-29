class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        # at each step, we need to compute the longest
        # increasing subsequence from this index.
        # at each step, if this is greater than prev, we can
        # continue an existing one, and if it's less than prev, then we can start a new one

        # let's do this top-down

        # instead of storing the prev in our recursive state,
        # we can actually just implicitly perform our state transfer
        # in our recursive call in our for loop
        
        # track which nums are valid
        valid = [True] * len(nums)
        memo = {}
        def dfs(i):
            
            if i in memo:
                return memo[i]
            #print(i)
            # no explicit base case
            # at this step, loop through all values in nums from i
            # and explore that option
            total = 1
            for j in range(i+1, len(nums)):
                # explore this state
                if nums[j] > nums[i]:
                    # continue this state
                    #print(f"Continuing from {i} to {j}")
                    total = max(total, 1 + dfs(j))
            
            #print(i, total)
            memo[i] = total
            return total
        return max(dfs(i) for i in range(len(nums)))

