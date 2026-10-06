class Solution:
    def canJump(self, nums: List[int]) -> bool:
        # at each step, we need to explore as far as we can?
        # at each step, track the farthest we can explore
        # from this index? if we ever reach the point where
        # current == farthest at the end of a loop execution
        # that means we can't go further, so return false?
        # farthest = max(farthest, i + nums[i])
        i = 0
        farthest = 0
        while i <= farthest and i < len(nums):
            farthest = max(farthest, i+nums[i])
            i+=1
        return i >= len(nums)