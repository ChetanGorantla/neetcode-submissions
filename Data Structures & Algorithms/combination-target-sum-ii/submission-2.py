class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        
        result = []
        candidates.sort()
        print(candidates)
        def backtrack(i, currsum, path):
            if (currsum == target):
                result.append(path.copy())
                return
            if (i >= len(candidates)):
                return
            if (currsum > target):
                return
            
            path.append(candidates[i])
            backtrack(i+1, currsum+candidates[i], path)
            path.pop()
            #recurse until you find the last duplicate of current val
            while (i+1 < len(candidates) and candidates[i] == candidates[i+1]):
                i+=1
            backtrack(i+1, currsum, path)



            
        backtrack(0, 0, [])
        return result
