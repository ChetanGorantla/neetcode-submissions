class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        # the total sum would be 2^n -1
        # where n is the length of the list
        # so to find the missing integer we just need to subtract everything
        n = len(nums)
        total = (n * (n+1))/2

        for num in nums:
            total-=num
        
        return int(total)