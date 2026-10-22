class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        # naive to continually divide by 2
        # look at bit pattern
        # only top bit should be set
        # all lower bits should be 0

        # isnt this the same time complexity
        if n < 1:
            return False
        while n > 1:
            curr = n & 1
            if curr:
                return False
            n = n>>1
        return True