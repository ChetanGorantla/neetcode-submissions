class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        result = []

        def backtrack(path, available):
            if (len(path) == len(nums)):
                result.append(path.copy())
                return
            for i in range(len(nums)):
                #loop thru each value in nums and add to permutation
                #if its not visited yet
                if (available[i]):
                    path.append(nums[i])
                    available[i] = False
                    backtrack(path, available)
                    path.pop()
                    available[i] = True
        backtrack([], [True]*len(nums))
        return result

        


        