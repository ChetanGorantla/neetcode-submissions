class Solution:
    def rob(self, nums: List[int]) -> int:
        # perhaps we run it twice and start at different points?
        # and then choose the maximum between the two runs?
        # one run is where we start at the first house
        # one run is where we start at the second house

        if len(nums) == 1:
            return nums[0]
        
        # first run
        first = 0
        second1 = 0
        for num in nums[0:-1]:
            temp = max(first + num, second1)
            first = second1
            second1 = temp
        
        # second run
        first = 0
        second2 = 0
        for num in nums[1:]:
            temp = max(first + num, second2)
            first = second2
            second2 = temp
        
        return max(second1, second2)