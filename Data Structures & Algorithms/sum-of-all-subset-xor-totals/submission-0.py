class Solution:
    def subsetXORSum(self, nums: List[int]) -> int:
        # generate all subsets
        # go based on index
        # get the xor totals if we add this element to the next subsets
        # and if we exclude
        # inclusion exclusion principle

        # what is our base case?
        # 
        def compute(i, total):
            
            if i == len(nums):
                return total
            
            return compute(i+1, total ^ nums[i]) + compute(i+1, total)

        return compute(0,0)