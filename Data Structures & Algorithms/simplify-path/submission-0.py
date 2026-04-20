class Solution:
    def simplifyPath(self, path: str) -> str:
        stack = []

        tokens = path.split("/")
        print(tokens)
        for token in tokens:
            if token == '':
                continue
            
            # process an actual value
            if token == ".":
                continue

            # append the current part
            
            
            if token == "..":
                if stack:
                    stack.pop()
            else:
                stack.append(token)
        
        return "/" + "/".join(stack)


            