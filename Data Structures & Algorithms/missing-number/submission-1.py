class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        # xor is associative and commutative
        # so if we xor all numbers from 0 to n and all values inside nums
        # the result will be the missing value
        
        n = len(nums)
        xor = n
        for i in range(n):
            xor ^= (i ^ nums[i])
        
        return xor