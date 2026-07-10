class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        # sliding windopw
        c = 0
        l = 0
        r = 0
        prod = 1
        for r in range(len(nums)):
            # at every "iteration" there is a valid window, we just need to compress it

            prod *= nums[r]
                
            while prod >= k and l <= r:
                prod //= nums[l]
                l+=1
            
            # once we've compressed, compute the # of subwindows
            c+=(r-l+1)
            
        return c