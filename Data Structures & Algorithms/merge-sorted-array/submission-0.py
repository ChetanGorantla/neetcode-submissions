class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        # maintain an index of where we are in nums2
        
        for i in range(m, len(nums1)):
            nums1[i] = nums2[i-m]
        nums1.sort()