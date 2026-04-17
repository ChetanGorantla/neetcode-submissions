class Solution:
    def isHappy(self, n: int) -> bool:
        found = set()
        while n != 1:
            if n in found:
                return False
            found.add(n)
            temp = n
            squares = 0
            while (temp > 0):
                squares += (temp % 10) ** 2
                temp = int(temp/10)
            
            n = squares

        return True