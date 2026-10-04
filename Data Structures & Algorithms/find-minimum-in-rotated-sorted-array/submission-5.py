class Solution:
    def findMin(self, nums: List[int]) -> int:
        # we need to find the minimum in the rotated sorted array
        # at each l and r, have an m
        # if l < m, the partition could live on the right
        # within that, if m < r

        # if l < m, if m > r, the partition exists on the right
        # if m < r, the partition lives on the left

        # if l > m, if m 

        # if m > r, the partition must live on the right
        # if m < l, the partition must live on the left
        l = 0
        r = len(nums)-1

        while l < r:
            m = (l+r)//2
            if nums[m] > nums[r]:
                l=m+1
            else:
                r = m
        
        return nums[l]