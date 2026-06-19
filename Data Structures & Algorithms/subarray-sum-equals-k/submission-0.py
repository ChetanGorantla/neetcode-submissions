class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        # at each step we want to see how many times currSum-k has occured before us
        total = 0
        currSum = 0
        prefixes = {0:1}

        for num in nums:
            currSum += num
            lf = currSum-k
            total += prefixes.get(lf, 0)
            
            prefixes[currSum] = 1 + prefixes.get(currSum, 0)
        
        return total