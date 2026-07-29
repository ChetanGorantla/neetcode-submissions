class Solution:
    def canPartitionKSubsets(self, nums: List[int], k: int) -> bool:
        # sums are all equal means we have to match k distinct targets of sum(nums)/k

        # we need to track how many more subsets we need to fulfill
        # if our current target is 0 and our remaining subsets to fill is 0
        # that's our base case, return true
        # if our current target < 0 return False, this was an invalid path
        # at each step, we want to survey all possible non-taken nums
        # and try to add that to our subset

        global_target = sum(nums)//k

        # unable to be split evenly
        if global_target != sum(nums)/k:
            return False
        
        visited = [False for _ in range(len(nums))]
        print(global_target)
        #counter = 0
        nums.sort(reverse = True)


        # i maintains our current position in our current pass
        # k denotes which pass we are in
        # curr_sum maintains what our running total is for this pass
        def backtrack(i, k, curr_sum):
            # no more subsets to fill
            if k == 0:
                return True

            # there are more subsets to fill
            # we need to check to see if our current sum fits our goal
            if curr_sum == global_target:
                # start a new pass
                return backtrack(0, k-1, 0)
            
            # we have not filled our target yet for this pass
            # explore from i until the end
            for j in range(i, len(nums)):
                # try this value if it's not visited yet
                # skip this value if it's used or if it'll exceed our threshold
                if visited[j] or curr_sum + nums[j] > global_target:
                    continue
                
                # this value is valid, try this
                visited[j] = True
                if backtrack(j+1, k, curr_sum + nums[j]):
                    return True
                visited[j] = False
            return False

    
        return backtrack(0, k-1, 0)

                    

        