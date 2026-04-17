class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        # initialize count as 0
        # check if every digit is 9
        
        out = [0 for _ in range(len(digits)+1)]

        c = 1
        i = len(digits)-1
        while (i >= 0):
            # get sum
            curr = digits[i]+c
            digit = (curr) % 10
            c = int((curr)/10)
            out[i+1] = digit
            i-=1
        
        out[0] = c
        if not c:
            return out[1:]
        return out

