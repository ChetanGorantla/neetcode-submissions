class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        # first let's just think of this in terms of backtracking
        # at each value, if it is greater than the previous sequence value, we choose
        # whether or not to include this in the upcoming path.
        # maybe we can memoize based on longest subsequence from an index?
        # memoize the length of the subsequence from this index to the end of the array?

        # store memo items as index : length
        memo = {}
        
        def search(idx, prev, length):
            if idx >= len(nums):
                return length
            
            if idx in memo:
                return memo[idx]
            
            # don't include this value
            skip = search(idx+1, prev, length)
            # if this is optimal, include it
            
            if prev == -1 or nums[idx] > nums[prev]:
                include = search(idx+1, idx, length+1)
            else:
                include = length
            maximum = max(include, skip)
            # add the tuple if not existing
            if (prev, idx) in memo:
                memo[(prev, idx)] = max(memo[(prev, idx)], maximum)
            else:
                memo[(prev, idx)] = maximum

            return maximum
        
        val = search(0, -1, 0)
        #print(memo)
        return val



        