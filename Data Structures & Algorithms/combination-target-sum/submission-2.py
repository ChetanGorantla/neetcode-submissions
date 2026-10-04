class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        # at this step, we can only take this or next elements
        # choose one and continue from there
        # populate a running total, path, and index
        out = []
        def explore(i, total, path):
            if total == target:
                out.append(path.copy())
                return
            
            if total > target:
                return
            
            
            for j in range(i, len(nums)):
                path.append(nums[j])
                explore(j, total+nums[j], path)
                path.pop()
            
        explore(0, 0, [])
        return out