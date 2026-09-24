class Solution:
    def rob(self, nums: List[int]) -> int:
        # we can either start from the 0th house or the 1th house
        # find the max between both
        # restrict the window from 0->n-2, 1->n-1
        if len(nums) == 1:
            return nums[0]
        
        if len(nums) == 2:
            return max(nums[0], nums[1])

        def compute(l, r):
            n2 = 0
            n1 = nums[l]
            for i in range(l+1, r):
                # curr max is either n1 or n2 + curr
                curr = max(n1, n2 + nums[i])
                print(i, curr)
                n2 = n1
                n1 = curr
            
            return n1
        
        return max(compute(0, len(nums)-1), compute(1, len(nums)))
