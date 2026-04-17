class Solution:
    def longestPalindrome(self, s: str) -> str:
        # the starting point of a call should be the center string
        # this center string has 2 cases, where our palindrome has either odd or even length
        # for odd length, the center string is just the middle char
        # for even length, the center string is the middle character and the one adjacent to the right
        # (if possible (not possible for last char))

        # now that we have this center string, we can only pursue if it is a palindrome
        # if it is not a palindrome, exit
        # if it is a palindrome, update the maximum

        result = s[0]
        maxlen = 1
        padded = " " + s + " "

        def search(l, r):
            nonlocal result
            nonlocal maxlen

            if l <= 0 or r >= len(padded)-1:
                return
            
            # this is in bounds. update our max and update the middle
            # only pursue this route if it's currently a palindrome

            if padded[l] == padded[r]:
                # we don't actually need to define the middle, we can just use math to compute
                # the length of the current palindromic substring, and just check the pointers
                # to continue down this path if it is correct
                #print("Pursuing " + middle)
                if r-l+1 > maxlen:
                    
                    maxlen = r-l+1
                    result = padded[l:r+1]
                    print("Updating result to be " + result)
                    
                search(l-1, r+1)
        
        for i in range(1, len(padded)-1):
            print("Calling method on " + padded[i])
            search(i, i)
            print("Calling method on " + padded[i:i+2])
            search(i, i+1)
        
        return result
        
