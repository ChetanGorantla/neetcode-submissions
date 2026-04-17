class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        out = []
        
        def dfs(i, curr, length):
            
            if (length > k):
                
                out.append(curr.copy())
                return
                #curr = []
                #dfs(i, curr, 0)
                #add and reset
            if (i > n):
                return
                #reached end, no more combinations to look for

            #actual logic
            curr.append(i)
            
            dfs(i+1, curr, length+1)
            curr.pop()
            
            dfs(i+1, curr, length)
        dfs(1, [], 1)
        return out
            
        