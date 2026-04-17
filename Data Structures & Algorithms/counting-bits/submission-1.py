class Solution:
    def countBits(self, n: int) -> List[int]:
        out = [0 for _ in range(n+1)]
        # this is kinda like a dp problem
        # we need to bitshift and count the number of bits in this bitshifted value
        # because this represents the previous state
        # each value should be 1 + count(bitshift)


        # sorry not the bitshifted value, the lower priority bits
        # how do we extract the lower priority bits given a byte?
        # subtract from the highest power of 2 smaller than this value

        for i in range(len(out)):
            out[i] = out[i >> 1] + (i & 1)
        
        return out