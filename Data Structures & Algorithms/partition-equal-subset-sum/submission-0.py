class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        # compute the overall sum and divide it by 2
        # this is the sum of the inidividual subsets
        # check to see if we can find 2 distinct subsets that sum up to that value

        # track the [idx][sum] for memo and store t/f
        tgt = 0
        for num in nums:
            tgt+=num
        if tgt % 2 == 1:
            return False
        
        tgt/=2
        tgt = int(tgt)

        memo = [[False for i in range(tgt+1)] for j in range(len(nums))]

        def search(idx, currSum):
            if idx >= len(nums):
                return False
            if currSum > tgt:
                return False
            if currSum == tgt:
                memo[idx][currSum] = True
                return True
            if memo[idx][currSum]:
                return True
            
            # we have not explored this yet.
            # we need to skip and explore this value
            if (search(idx+1, currSum) or search(idx+1, currSum + nums[idx])):
                memo[idx][currSum] = True
                return True
            
            return False
        
        return search(0,0)