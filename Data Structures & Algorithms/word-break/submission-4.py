class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        # backtrack linearly
        # at each index, do .contains on all words in the string
        # if the index of that .contains method is not 0, don't consider it
        # out of all the words that the indexOf is 0, search these options
        # keep track of your starting index
        # replace 0 with l so you don't have to splice strings each time
        # update l with l + len(word)
        # if l is equal to the length of the string, return true

        # keep a memo array to track if the rest of this array can be filled
        # after backtracking, reset that value

        # or keep a set tracking the l values that are able to reach the end successfully?
        # 

        # sort wordDict in terms of decreasing length
        wordDict = sorted(wordDict, key=len, reverse=True)
        bad = set([])
        def explore(l):
            if l == len(s):
                return True
            if l in bad:
                return False

            # explore all combinations
            overall = False
            for word in wordDict:
                if s.startswith(word, l):
                    if explore(l + len(word)):
                        return True
            # unable to find any matches
            bad.add(l)
            return overall
        
        return explore(0)
