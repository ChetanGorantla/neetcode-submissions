class Solution:
    def climbStairs(self, n: int) -> int:
        # the # of ways to reach a step is 
        # the # of ways to reach n-1 and n-2 combined
        n1 = 1
        n2 = 2
        if n == 1:
            return n1
        
        for i in range(2, n):
            # n2 += n1
            temp = n2
            n2 += n1
            n1 = temp
        
        return n2
