class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        if len(tokens) == 1:
            return int(tokens[0])
        stack = []
        for i in range(0,len(tokens)):
            token = tokens[i]
            stack.append(token)
            
            if token in ["+", "-", "*", "/"]:
                stack.pop()
                second = int(stack[-1])
                stack.pop()
                first = int(stack[-1])
                stack.pop()
                val = 0
                print(str(first) + token + str(second) + "=")
                if token == "+":
                    val = first+second
                    stack.append(val)
                if token == "-":
                    val = first-second
                    stack.append(val)
                if token == "*":
                    val = first*second
                    stack.append(val)
                if token == "/":
                    val = int(first/second)
                    stack.append(val)
                print(val)
        return stack[-1]
                

        
            