class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        result = []
        
        def backtrack(i, currsum, path):
            if (currsum > target):
                return
            if (target == currsum):
                result.append(path.copy())
                return
            if (i >= len(nums)):
                return
            
            #add current again
            path.append(nums[i])
            backtrack(i, currsum+nums[i], path)

            #add next one
            path.pop()
            backtrack(i+1, currsum, path)
            
        backtrack(0, 0, [])
        return result


            
            
