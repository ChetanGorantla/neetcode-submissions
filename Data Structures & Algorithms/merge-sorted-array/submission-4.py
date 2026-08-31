class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        # maintain an index of where we are in each array and add as necessary
        if m == 0:
            nums1[:] = nums2
            return

        i = 0 # nums1_copy
        j = 0 # nums2
        k = 0 # nums1

        nums1_copy = nums1[:m]
        while k < m+n:
            print(i,j,k)
            if i < len(nums1_copy) and (j == len(nums2) or nums1_copy[i] < nums2[j]):
                nums1[k] = nums1_copy[i]
                i+=1
            elif j < len(nums2) and (i == len(nums1_copy) or nums1_copy[i] >= nums2[j]):
                nums1[k] = nums2[j]
                j+=1
            k+=1
        
        
