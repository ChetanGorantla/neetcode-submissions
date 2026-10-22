class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        # naive to continually divide by 2
        # look at bit pattern
        # only top bit should be set
        # all lower bits should be 0

        # isnt this the same time complexity
        
        
        # 1000100 -> False
        # how to immediately know if there's 1 from n-1 to 0
        # mask with 1...1
        
        # n-1 will flip the first set bit
        # that means that if the flip flips a non n bit
        # then we return False
        return n > 0 and not (n & (n-1))