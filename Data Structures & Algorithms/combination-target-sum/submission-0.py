class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []

        curr = []
        
        #select current, or move to the next
        def dfs(i, curr, total):
            if (total == target):
                res.append(curr.copy())#matched target sum
                return
            

            if (i >= len(nums)):
                return#didnt find it
            
            if (total > target):
                return#exceeded sum
            

            curr.append(nums[i])
            dfs(i, curr, total + nums[i])
            curr.pop()
            dfs(i+1, curr, total)
        dfs(0, [], 0)
        return res

            
            
