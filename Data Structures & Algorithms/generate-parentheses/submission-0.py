class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        #either use stack to store current path, or use a string. i find string easier to understand
        res = []
        def backtrack(openN, closedN, path):
            if openN == closedN == n:
                res.append(path)
                #everything fulfilled (equal pairs)
                return
            
            if openN < n:
                #if you have available opens, add an open to satisfy
                backtrack(openN+1, closedN, path+"(")
                
            if closedN < openN:
                #if you have less closed than open, add a closed to match pairs
                
                backtrack(openN, closedN+1, path+")")
                
        
        backtrack(0,0,"")
        return res
            

        