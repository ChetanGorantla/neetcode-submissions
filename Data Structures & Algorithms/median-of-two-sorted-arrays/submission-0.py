class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        A, B = nums1, nums2
        # keep A as the smaller one
        if len(B) < len(A):
            A,B = B,A
        
        # setup bounds for binary search
        total = len(A) + len(B)
        half = total // 2
        l, r = 0, len(A) - 1

        # know that a soln exists
        while True:
            i = (l+r) // 2 # index in A
            j = half-i - 2 # index in B

            Aleft = A[i] if i >= 0 else float("-infinity")
            Aright = A[i+1] if (i+1) < len(A) else float("infinity")
            Bleft = B[j] if j >= 0 else float("-infinity")
            Bright = B[j+1] if (j+1) < len(B) else float("infinity")

            # partition is correct
            if Aleft <= Bright and Bleft <= Aright:
                # odd
                if total % 2 == 1:
                    return min(Aright, Bright)
                else:
                    return (max(Aleft, Bleft) + min(Aright, Bright)) / 2
                
            elif Aleft > Bright:
                # too many elements in Aleft, partition left
                r = i-1
            else:
                l = i+1
