class Solution:
    def climbStairs(self, n: int) -> int:
        one = 1
        two = 2
        if n == 1:
            return one
        for i in range(2, n):
            temp = one
            one = two
            two += temp
        return two