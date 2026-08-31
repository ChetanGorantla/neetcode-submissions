class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        # maintain an index of where we canonically are
        # versus where we are looking to move duplicates
        # skip over duplicate values

        i = 0
        for j in range(1, len(nums)):
            if nums[i] != nums[j]:
                # we have not encountered a duplicate. add this to canonical
                i+=1
                nums[i] = nums[j]
        
        # i is the index of the last canonical value 
        return i+1