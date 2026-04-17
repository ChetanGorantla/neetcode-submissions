class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        out = []

        def backtrack(idx, path):
            # choose current val or choose next val to add to curr path
            if (idx == len(nums)):
                out.append(path.copy())
                return
            

            path.append(nums[idx])
            backtrack(idx+1, path)
            path.pop()
            backtrack(idx+1, path)
        
        backtrack(0,[])
        return out

            