class Solution:
    def maxFrequency(self, nums: List[int], k: int) -> int:
        # increments by 1
        # count the diffs?
        # sort one pass
        nums.sort()
        ct = 0
        i = 0
        
        # sliding window
        # the current window needs to have a total cap diff of <= k
        # if the window has a cap diff < k, shift right
        # if it has a cap diff > k, shift left

        cap_diff = 0
        l = 0
        r = 0
        while r < len(nums):
            #print(l, r)
            #print(cap_diff)
            # we have a window, and a cap_diff.
            # compute whether or not we want to shift l or r
            if cap_diff <= k:
                # valid window, update ct
                ct = max(ct, r-l+1)
                
                # won't find more optimal if already at end and met constraints
                if r == len(nums)-1:
                    return ct

                # initial cap diff was nums[r]-nums[l]
                # new cap diff is nums[r+1]-nums[l]
                # difference is nums[r+1]-nums[r] and the diff verticals
                cap_diff+=(nums[r+1]-nums[r]) * (r-l+1)
                r+=1
                
            else:
                cap_diff -= nums[r]-nums[l]
                l+=1
        return ct
            
        
        