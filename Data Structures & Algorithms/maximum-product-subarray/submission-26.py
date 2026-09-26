class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        # we have two options
        # we can either start a new subarray from here
        # or continue an existing one
        
        maxprod = -sys.maxsize

        # we need to maintain our positive multiple and our
        # negative multiple
        total = -sys.maxsize
        minimum = 1
        maximum = 1
        for num in nums:
            newmin = minimum * num
            newmax = maximum * num
            minimum = min(newmax, newmin, num)
            maximum = max(newmax, newmin, num)
            total = max(total, maximum)
        
        
        return total


            
