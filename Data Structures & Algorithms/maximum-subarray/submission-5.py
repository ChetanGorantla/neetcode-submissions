class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        # maintain a running sum
        # if the sum ever dips below 0, then reset the sum be zero
        
        maxsum = -sys.maxsize
        currsum = 0
        for num in nums:
            currsum += num
            print(currsum)
            maxsum = max(num, maxsum, currsum)
            if currsum < 0:
                currsum = 0
            
            
        
        # if maxsum == 0, we need to check what the actual max value is

        return maxsum