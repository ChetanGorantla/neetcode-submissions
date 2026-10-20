class Solution:
    def diffWaysToCompute(self, expression: str) -> List[int]:
        # dp based on the substring
        # at each step return all possible results

        # split the array by the delimeters
        tokens = re.split(r'([+\-*])', expression)
        memo = {}
        def dp(l, r):
            if (l, r) in memo:
                return memo[(l, r)]
            if l == r:
                return [int(tokens[l])]
            if l > r:
                return []
            
            # base cases complete. we have a range
            # we need to locate all possible splits
            # and perform dp on those splits
            arr = []
            for i in range(l+1, r, 2):
                # split based on i
                left = dp(l, i-1)
                right = dp(i+1, r)
                # join all combinations of left and right based on 
                # our operation at i
                
                for lc in left:
                    for rc in right:
                        if tokens[i] == "-":
                            arr.append(lc-rc)
                        elif tokens[i] == "+":
                            arr.append(lc+rc)
                        else:
                            arr.append(lc*rc)
            memo[(l,r)] = arr
            return arr
        
        return dp(0, len(tokens)-1)
