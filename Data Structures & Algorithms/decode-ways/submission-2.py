class Solution:
    def numDecodings(self, s: str) -> int:
        # base cases: if idx == len(s) return 0
        # at each step, we must consider two cases: take one digit or take 2 digits
        # before exploring, if the two digits are greater than 26 or starts with 0,
        # don't pursue that route
        # also if the one digit is 0, don't pursue that route
        
        # backtrack by storing how many possible ways we can decode a sequence
        memo = {}

        def explore(idx):
            if idx == len(s):
                return 1
            
            if idx in memo:
                return memo[idx]
            
            # we have not explored this index yet
            total = 0
            one = s[idx]
            two = " "
            if idx < len(s)-1:
                two = s[idx] + s[idx+1]
            
            if one != "0":
                total += explore(idx+1)
            
            print(two)
            if len(two) == 2 and two[0] != "0" and int(two) <= 26:
                total += explore(idx+2)
            
            memo[idx] = total
            return total

        return explore(0)