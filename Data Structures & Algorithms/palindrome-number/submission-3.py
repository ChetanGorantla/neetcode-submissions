class Solution:
    def isPalindrome(self, x: int) -> bool:
        # implement a stack
        # first half to populate the stack
        # second half to empty the stack

        # is there a way to do it in O(1) space? two pointer approach via math?

        # divide by converging powers of ten?
        # 111111
        # 100000
        # let n = # of digits - 1
        # check (x / 10^n) % 10 == (x/10) % 10
        # n--
        # 
        if x < 0:
            return False

        tmp = x
        n = 0
        while tmp > 0:
            tmp = int(tmp/10)
            n+=1
        
        # n stores # of digits in x

        i = 0

        while (i < n/2):
            lhs = int(x / (10 ** (n-1-i))) % 10
            rhs = int(x/(10**i)) % 10
            print(lhs, rhs)
            if lhs != rhs:
                return False
            i+=1
        
        return True
