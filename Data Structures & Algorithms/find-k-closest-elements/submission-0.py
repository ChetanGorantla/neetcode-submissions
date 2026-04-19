class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        # if curr < x, pop oldest (based on size cmp k) and insert newest
        
        # maintain l and r tracking our current window
        # shift this window through our entire array
        # compute some score to tell us if we are at the optimal or not
        # initial score from 0 to k
        # when shifting, subtract the score of l and add the score of r

        # at the start add score of r
        # at end subtract score of l
        # shift pointers

        # when checking to see if optimal, only compute if score > maxscore
        # use MINSCORE since we want to MINIMIZE distance

        l = 0
        r = k-1
        score = 0
        min_score = float('infinity')
        optimal_l = 0
        optimal_r = k-1

        for i in range(k-1):
            score += abs(x-arr[i])

        for i in range(k-1, len(arr)):
            score += abs(x-arr[r])

            
            if score < min_score:
                min_score = score
                optimal_l = l
                optimal_r = r
            
            print(score)
            print(optimal_l, optimal_r)
            score -= abs(x-arr[l])
            l+=1
            r+=1
        
        return arr[optimal_l:optimal_r+1]