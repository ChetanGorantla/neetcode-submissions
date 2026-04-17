class Solution:
    def hammingWeight(self, n: int) -> int:
        # bitshift 32 times
        count = 0
        for i in range(32):
            if n & 1 == 1:
                count+=1
            n = n >> 1
        return count