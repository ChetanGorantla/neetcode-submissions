class Solution:
    def maxUniqueSplit(self, s: str) -> int:
        # maintain a set
        # at each step, choose how many letters to include
        # in this substring
        # skip substrings that already live in set
        # backtrack
        # instead of looping over s loop over the split version
        # so we can join more efficiently when building substrings


        # at each step, return the # of pieces remaining from here
        # 1 + dfs(j+1)
        # cannot memoize because state depends on substrings previously generated
        # probably why n is low
        # 

        # we need to prune 
        # if len(substrings) + len(s)-i+1 < maxlen
        # then exit this scenario
        maxlen = 0

        def search(i, substrings):
            nonlocal maxlen

            if i == len(s):
                maxlen = max(maxlen, len(substrings))
                return
            
            # we are not at the end of the array 
            # we need to choose a substring from i to the end of s
            # if 

            if len(substrings) + len(s)-i <= maxlen:
                return

            for j in range(i, len(s)):
                curr = s[i:j+1]
                if curr not in substrings:
                    substrings.add(curr)
                    search(j+1, substrings)
                    substrings.remove(curr)
            
            
        
        search(0, set())
        return maxlen

