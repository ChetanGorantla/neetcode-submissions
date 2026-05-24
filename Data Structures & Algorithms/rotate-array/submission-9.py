class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        
        # left pointer at 0
        # right pointer at n-k
        n = len(nums)
        
        # k is not necessarily less than n, so wrap-arounds are symmetric
        k = k % n
        
        def reverse(l, r):
            while l < r:
                nums[l], nums[r] = nums[r], nums[l]
                l+=1
                r-=1
        
        reverse(0, n-1)
        reverse(0, k-1)
        reverse(k, n-1)
        
        

        
        