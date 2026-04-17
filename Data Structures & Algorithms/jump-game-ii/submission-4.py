class Solution:
    def jump(self, nums: List[int]) -> int:
        # maintain an array of minimum jumps
        # last index will be 0
        # at this index, we need to check, to go from i to i+1,
        # the minimum number of jumps is either 1 + jumps(i+1)
        # or 1 + jumps(i + jump_val)

        if len(nums) == 1:
            return 0

        jumps = [0 for _ in range(len(nums))]

        def getJumps(i):
            if i >= len(jumps) or i < 0:
                return 0

            print(f"Jumps for index {i}: {jumps[i]}")
            return jumps[i]

        for i in range(len(nums)-2, -1, -1):
            step = 1 + getJumps(i+1)
            jump = 1 + getJumps(i+nums[i])
            print(step, jump)
            min_jumps = min(step, jump)
            jumps[i] = min_jumps
        
        return jumps[0]
    
    