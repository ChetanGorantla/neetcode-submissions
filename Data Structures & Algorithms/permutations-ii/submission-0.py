class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        # return all possible permutations
        # first sort?
        # classic backtracking problem

        list.sort(nums)

        # once we explore, our return stage needs to move forward to the next value that isnt the same

        # how do we avoid duplicate permutations without forcing lookups?

        # wait
        # at each step, we have the option to either include curr in the permutation or exclude
        # first, how do you even generate all permutations again?
        
        results = []

        # maintain a list of choices remaining. use indices inside of that. make sure they're laid out based on
        # sorting order of their respective values
        # maintain a list of your current path
        # at each step, loop through the entire array to explore all options
        # but in your backtracking step, you must skip the value you just retrieved
        # i think i'm overthinking it

        # maybe keep a bool array of available/unavailable?
        # track to see, when we loop over a choice, if it's available
        # we can take it
        # if not, don't take it
        # backtrack as such
        # and just call dfs to the next index

        
        def dfs(i, permut, available):
            nonlocal results
            if i == len(nums):
                #print(available)
                if len(permut) == len(nums):
                    results.append(list.copy(permut))
            else:
                # not at the end
                # explore and then backtrack
                # we have to explore ALL of the options, right?

                for j in range(0, len(nums)):
                    if j > 0 and nums[j] == nums[j-1] and available[j-1]:
                        continue
                    if available[j]:
                        permut.append(nums[j])
                        available[j] = False
                        dfs(i+1, permut, available)
                        permut.pop()
                        available[j] = True
                
                # how can i force to avoid duplicates?
                # using the nature of the sorted array to jump past duplicates?
                

            
            

        dfs(0, [], [True for _ in range(len(nums))])
        return results


