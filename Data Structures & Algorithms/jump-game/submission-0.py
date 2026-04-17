class Solution:
    def canJump(self, nums: List[int]) -> bool:
        n = len(nums)
        # goal is initially the very last element
        # goal represents the last element needed to reach to reach the end of the list
        # we keep decreasing goal as we find more ways to reach goal
        goal = n-1
        for i in range(n-2, -1, -1):
            # if we can reach goal from here, update goal to be this index
            jump = nums[i]
            if i + jump >= goal:
                goal = i
            
        # return if goal == 0
        # (we can reach the end from first index)
        return goal == 0

        
        

        
