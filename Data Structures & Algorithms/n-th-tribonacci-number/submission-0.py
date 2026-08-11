class Solution:
    def tribonacci(self, n: int) -> int:
        # bottom-up space optimized
        # we need to store tn, tn_1, tn_2
        # Tn = Tn-1 + Tn-2 + Tn-3
        # add and shift
        tn = 1
        tn1 = 1
        tn2 = 0

        if n == 0:
            return tn2
        if n == 1:
            return tn1

        for i in range(2, n):
            # compute the sum of all three
            # store that in tn
            # 
            temp_n = tn
            temp_n1 = tn1
            tn+=tn1 + tn2
            tn1 = temp_n
            tn2 = temp_n1
        
        
        return tn