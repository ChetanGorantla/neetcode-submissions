class Solution:
    def knightDialer(self, n: int) -> int:
        # number of distinct digit sequences
        # this is a forced property based on the permutation
        # no need to sort or anything
        # need to maintain a 2d array
        
        
        # at each step, look at where we currently are, and how many 
        # numbers we currently have left to fill
        # memoize how many possible sequences can be made to get to
        # n
        # so we don't actually store a current index
        # we just store our remaining count
        # and survey all digits
        # maybe we just keep that implicit?
        # at each step compute how many valid sequences start from
        # this digit and reach the end
        # we need to store two states
        # the current digit and the # of digits left to populate
        # current digit takes on the form of r, c
       

        # model this as a graph
        # at each step, populate how many ways we can reach each digit
        MOD = 1000000007

        dp = [1]*10
        adjacency = {
            0:[4, 6],
            1:[6, 8],
            2:[7, 9],
            3:[4, 8],
            4:[3, 9, 0],
            5:[],
            6:[1, 7, 0],
            7:[2, 6],
            8:[1, 3],
            9:[2, 4]
        }

        for i in range(n-1):
            new_dp = [0]*10
            for num in range(10):
                for val in adjacency[num]:
                    new_dp[num]+=dp[val]
            dp = new_dp
        
        return sum(dp)%MOD
        
        
