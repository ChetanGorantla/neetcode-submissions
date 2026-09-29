class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        # we need to split sum into target (target = sum//2)
        # if we can find one target, return true
        # we don't need to find the second target because that's implicit

        totalsum = sum(nums)
        target = totalsum//2
        if target * 2 != totalsum:
            return False
        

        # see if we can find a sum of target from here
        # do this with dp

        # instead of tracking the index we're at, let's rather 
        # track our current sum

        # we need to memoize the bitmask of our visited array?
        n = len(nums)
        memo = {}
        def dp(tgt, mask):
            if tgt == 0:
                return True
            if mask in memo:
                return memo[mask]
            # tgt isn't found yet
            # we need to look at all possible values we haven't explored yet
            possible = False
            # 0 0 0
            #   1
            for i in range(n):
                # for each index 0..n-1
                # we need to decide if this value is set
                # if the value is already in use or > tgt, can't use it
                if ((mask >> n-i-1) & 1) or nums[i] > tgt:
                    continue

                # the value isn't set. try to use it
                newmask = mask | (1 << n-i-1)
                possible = possible or dp(tgt-nums[i], newmask)
            memo[mask] = possible
            return possible
        
        return dp(target, 0)
                


            
