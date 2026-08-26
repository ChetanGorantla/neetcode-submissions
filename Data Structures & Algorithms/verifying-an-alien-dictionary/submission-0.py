class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        # just compare adjacent words
        # compare characters between a and b
        # if they are equal, continue down
        # if a[i] < b[i], this is a success. go to the next words.
        # if a[i] > b[i], this is a failure. return false.
        # we need to ensure we don't go out of bounds. set the space of search to be the min between the
        # lengths of a and b.
        # at the end of all comparisons between a and b, if one of the indices is equal to the length,
        # that means that one of the words is a prefix of the other one.
        # that means we need to see if b is the prefix of a.
        # if len(b) > len(a), return false
        # otherwise, continue on because a was the prefix of b (correct)

        indices = {}
        for i in range(len(order)):
            indices[order[i]] = i
        
        for i in range(len(words)-1):
            a = words[i]
            b = words[i+1]
            # we need to compare a and b
            j = 0
            while j < min(len(a), len(b)):
                pos_a = indices[a[j]]
                pos_b = indices[b[j]]
                # if we are in order, this is correct. you can exit this case.
                if pos_a < pos_b:
                    break
                elif pos_a > pos_b:
                    # we are out of order. this is false
                    return False
                else:
                    # these are equivalent. go down the line
                    j+=1
            # check to see if j is equal to the length
            if j == min(len(a), len(b)) and len(a) > len(b):
                return False
                # this means b is a prefix of a
        return True
                

                
