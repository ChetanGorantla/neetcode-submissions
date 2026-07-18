class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        # return the number of possible combinations that add up to target
        # you can reuse numbers
        # sort the array first so we reach base cases faster

        # break out if the current sum is greater than target or if there's no more to inspect
        # at each step we need to explore all unchosen
        # this means we need to maintain a visited bool array

        # at each step we must take this value
        # we have the choice for extension
        # we can either continue with the current value
        # or jump to a different value
        # meaning we just need to loop over everything
        # explore all options that are unvisited
        nums = sorted(nums)
        

        # think of it as if you're trying to fill in the gap

        memo = {}
        # store what you can retry also
        def search(remaining):
            if remaining in memo:
                return memo[remaining]
            if remaining == 0:
                return 1
            
            # re-explore curr
            combinations = 0
            for num in nums:
                if num > remaining:
                    break
                combinations += search(remaining-num)
            
            
            memo[remaining] = combinations
            return combinations
        
        return search(target)
            
                