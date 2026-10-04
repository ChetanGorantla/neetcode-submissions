class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l = 0
        r = len(nums)-1
        if len(nums) == 1:
            return 0 if nums[0] == target else -1
        while l < r:
            m = (l+r+1)//2

            if nums[m] == target:
                return m
            
            # we are not equal to the target
            # we need to locate where the partition is
            if nums[m] < nums[l]:
                # the partition occurs on the left side
                if nums[m] <= target <= nums[r]:
                    l = m
                else:
                    r = m-1
            else:
                # the partition occurs on the right side
                if nums[l] <= target <= nums[m]:
                    r = m-1
                else:
                    l = m
        return -1 if nums[l] != target else l
                