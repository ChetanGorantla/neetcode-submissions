class Solution:
    def checkValidString(self, s: str) -> bool:
        # we need to maintain a stack of the open brackets
        # and the stars.
        # once we find a right parenthesis, we check to see if the 
        # open bracket queue is nonempty. if so, we want to pop from there
        # because we have fulfilled a parenthesis pair
        # if it's empty, we need to use up a star
        # if both are empty, return false

        # at the very end, we have exhausted all of our possible pairs
        # try to pair up the remaining values
        # pop the indices of the rightmost left parenthesis and stars
        # if the stars parenthesis are before the left, return false
        # otherwise return false

        opens = []
        stars = []

        for i in range(len(s)):
            char = s[i]
            if char == "*":
                stars.append(i)
            elif char == "(":
                opens.append(i)
            else:
                # this is a closing bracket. we need to pop from something
                # or return false
                

                # pop from whichever exists first
                if opens or stars:
                    if opens:
                        opens.pop()
                    elif stars:
                        stars.pop()
                else:
                    return False
                
        # at the end keep popping until we can't pop anymore
        # and make sure that the indices are matching
        print(opens, stars)
        while opens and stars:
            open_i = opens.pop()
            stars_i = stars.pop()
            if open_i > stars_i:
                return False
        
        return len(opens) == 0



                

