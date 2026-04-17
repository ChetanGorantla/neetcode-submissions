class Solution:
    def rob(self, nums: List[int]) -> int:
        # if curr + second > first, update curr to curr + second
        # if curr + second <= first, maintain everything?
        # shift second and first

        second = nums[0]
        if len(nums) == 1:
            return second
        first = nums[1]
        
        if len(nums) == 2:
            return max(first, second)
        
        if second > first:
            first = second
            
        for i in range(2, len(nums)):
            
            if nums[i] + second >= first:
                nums[i] += second
            else:
                nums[i] = first
            temp = first
            first = nums[i]
            second = temp
        print(nums)
        return max(first, second)