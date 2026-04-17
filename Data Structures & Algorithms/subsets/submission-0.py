class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []

        subset = []
        def dfs(i):
            if i >= len(nums):
                res.append(subset.copy())
                return

            #decision to include nums[i] (left decision)
            subset.append(nums[i])
            dfs(i+1)

            #decision NOT to include nums[i] (right decision)
            subset.pop()#pop the one i just added
            dfs(i+1)
        dfs(0)
        return res

            