class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        minimum = 1
        maximum = 0
        globalmax = nums[0]
        for num in nums:
            # 3 cases. Either start a new subarray, or continue the previous one
            # when continuing the previous one, we can either continue the minimum route, or
            # the maximal route.
            newmin = minimum * num
            newmax = maximum * num
            minimum = min(newmax, min(newmin, num))
            maximum = max(newmax, max(newmin, num))
            print("min: " + str(minimum))
            print("max: " + str(maximum))
            globalmax = max(globalmax, maximum)

        
        if globalmax == 0:
            # find overall array max
            overallmax = -1 * sys.maxsize
            for num in nums:
                overallmax = max(overallmax, num)
            return overallmax
        return globalmax