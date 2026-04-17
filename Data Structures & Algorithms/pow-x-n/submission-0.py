class Solution:
    def myPow(self, x: float, n: int) -> float:
        
        if n > 0:
            out = 1
            while n > 0:
                out *= x
                n-=1
        else:
            out = 1
            while n < 0:
                out *= (1/x)
                n+=1
        return out