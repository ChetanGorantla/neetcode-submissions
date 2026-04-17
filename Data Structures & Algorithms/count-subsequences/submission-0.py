class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        # keep memoized tracker of index in t, and number of ways to continue the string from that index


        # at each step we check to see if numChars is equal to the length of target
        # and if so, return 1

        # if in memo return result

        # in our recursive step, we need to either include this char or not include it

        # if this char in s is matching in t, then we choose to include it

        # either way we also choose to not include it

        # and sum up both of these values and store it in memo
        
        memo = {}

        def search(l, r, numMatchingChars):
            if numMatchingChars == len(t):
                return 1
            
            # if out of bounds exit
            if l >= len(s) or r >= len(t):
                return 0
            
            if (l, r) in memo:
                return memo[(l,r)]

            # not explored yet
            
            total = 0
            if s[l] == t[r]:
                # include this
                total += search(l+1, r+1, numMatchingChars+1)
            # regardless we want to explore without choosing
            total += search(l+1, r, numMatchingChars)

            memo[(l, r)] = total
            return total
        
        return search(0, 0, 0)


    