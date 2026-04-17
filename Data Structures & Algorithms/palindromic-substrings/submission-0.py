class Solution:
    def countSubstrings(self, s: str) -> int:
        # we basically need to store a set of tuples, where each tuple contains the l and r pointer
        # we count the middle positions
        palindromes = set([])
        padded = " " + s + " "
        def search(l, r):
            # if l and r are out of bounds, escape
            if l <= 0 or r > len(s):
                return
            if padded[l] == padded[r]:
                # expand outwards
                palindromes.add((l, r))
                search(l-1, r+1)
        
        # do single and double counting
        for i in range(1, len(padded)):
            search(i,i)
            search(i,i+1)
        print(palindromes)
        return len(palindromes)