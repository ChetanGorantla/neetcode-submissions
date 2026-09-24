class Solution:
    def rob(self, nums: List[int]) -> int:
        # at each step, the max money at this step is either
        # the previous max
        # or the -2 max + this

        for i in range(1, len(nums)):
            take = 0 if i-2 < 0 else nums[i-2]
            skip = nums[i-1]
            nums[i] = max(take + nums[i], skip)
        
        return nums[-1]