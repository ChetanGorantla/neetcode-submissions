class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        # as long as our current subarray is >= 0, we can continue with this sum
        
        # if adding this number would make our total < 0, don't add it. instead jump
        total = 0
        maxtotal = -1001
        for i in range(len(nums)):
            total += nums[i]
            maxtotal = max(total, maxtotal)
            if total < 0:
                total = 0
        return maxtotal
            
