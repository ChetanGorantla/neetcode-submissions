class Solution:
    def getSum(self, a: int, b: int) -> int:
        # get & 1 to extract last digit
        # bitshift digits to the right

        # based on the carry-over and the two digits, determine what to put as the next bit
        # and assign as the next carry-over
        carry = 0
        out = 0
        for i in range(32):
            l = (a >> i) & 1
            r = (b >> i) & 1
            
            # figure out what bit and carry is
            bit = l ^ r ^ carry

            
            carry = (l & r) | (l & carry) | (r & carry)

           
                
            # bit is what we are adding
            out = out | (bit << i)
        
        if out >= 2 ** 31:
            out -= 2**32
        
        return out