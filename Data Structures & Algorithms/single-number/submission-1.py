class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        # keep a running total of xor
        xor = 0
        for i in range(len(nums)):
            xor = nums[i] ^ xor
        
        return xor
