class Solution:
    def maxUniqueSplit(self, s: str) -> int:
        # maintain a set
        # at each step, choose how many letters to include
        # in this substring
        # skip substrings that already live in set
        # backtrack
        # instead of looping over s loop over the split version
        # so we can join more efficiently when building substrings

        arr = list(s)

        # at each step, return the # of pieces remaining from here
        # 1 + dfs(j+1)
        # cannot memoize because state depends on substrings previously generated
        # probably why n is low
        # 
        def search(i, substrings):
            if i == len(arr):
                return 0
            
            # we are not at the end of the array 
            # we need to choose a substring from i to the end of s
            maxpieces = 0
            for j in range(i, len(arr)):
                curr = "".join(arr[i:j+1])
                if curr not in substrings:
                    substrings.add(curr)
                    maxpieces = max(maxpieces, 1+search(j+1, substrings))
                    substrings.remove(curr)
            
            return maxpieces
        
        return search(0, set())

