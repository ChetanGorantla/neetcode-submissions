class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        # keep a running total of xor
        xor = nums[0]
        for i in range(1, len(nums)):
            xor = nums[i] ^ xor
        
        return xor
