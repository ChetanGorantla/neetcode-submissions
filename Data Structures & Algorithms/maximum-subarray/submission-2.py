class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        maximum = nums[0]
        running = 0
        for num in nums:
            running += num
            running = max(0, running)
            maximum = max(maximum, running)
        
        if maximum == 0:
            return max(nums)
        return maximum