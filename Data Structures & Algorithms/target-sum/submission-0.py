class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        # at each step, we can either add or subtract it
        # memoize based on the index in the array and the current sum
        # store the number of ways to reach target from this index and sum

        # base cases:
        # if our current sum = target, return 1
        # if our index is out of bounds, return 0
        # otherwise, we have not explored this yet

        memo = {}

        def search(idx, curr):
            
            # our condition can only be met if we have searched thru the entire array
            if idx == len(nums):
                if curr == target:
                    return 1
                else:
                    return 0
            
            if (idx, curr) in memo:
                return memo[(idx, curr)]


            # we have not explored this yet
            # we can either add or subtract this value
            ways = search(idx+1, curr+nums[idx]) + search(idx+1, curr-nums[idx])
            memo[(idx, curr)] = ways
            return ways
        
        return search(0, 0)
        
