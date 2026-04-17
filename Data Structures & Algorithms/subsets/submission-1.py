class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        result = []

        current_path = []
        def backtrack(i):
            if (i >= len(nums)):
                result.append(current_path.copy())
                
                return
            
            current_path.append(nums[i])
            backtrack(i+1)

            current_path.pop()
            backtrack(i+1)
        backtrack(0)

        return result

            

            