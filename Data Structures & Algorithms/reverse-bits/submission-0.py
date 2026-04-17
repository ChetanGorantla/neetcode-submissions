class Solution:
    def reverseBits(self, n: int) -> int:
        # create an unsigned integer as the result
        # keep bitshifting right for n, and extract the bit that was shifted out
        # how do we track what bit was shifted out?
        # we can do curr & 1 before shifting, which will tell us what the bit was
        # and then how do we append it to the new integer?
        # bitshift once to the left, and do | bit
        # this will insert whatever bit needs to be appended
        # keep doing this for the entire unsigned int
        # there will be an extra 0 at the end which is fine

        result = 0
        # if we do while n instead of looping thru each unsigned bit, we might encounter an issue
        # where it sees that the rest of n is 0 so it stops, but we really need to have kept
        # appending those zeros. let's see

        for i in range(32):
            bit = n & 1
            #print(bit)
            n = n >> 1
            result = result << 1
            result = result | bit
        
        return result