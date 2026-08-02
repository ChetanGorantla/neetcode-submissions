class Solution:
    def decodeString(self, s: str) -> str:
        # keep track of saved
        # when we pop a number we need to repeat saved by x amount of times
        # recursive
        # we have a multiplier that continuously grows
        # every time we encounter a closing bracket we divide the multiplier by stack.pop
        # each time we encounter a character we repeat it x multiplier
        # each time we encounter an opening bracket we skip
        # each time we encounter a number we multiply multiplier by int(curr)

        # populate the stack with individual multipliers

        # need to include recursion in this approach
        # can we completely revise it to be just recursion?
        
        
        # do a one pass where you search for closing brackets and maintain a stack
        # so that whenever you find a closing bracket you pop from the stack
        # and call recursion on that
        # we need to go by windows?
        # or maybe we need to maintain a running string of what we're multiplying?
        # no we can't maintain a running string because that's greedy
        # we cannot be greedy we must generate windows altogether recursively
        # whenever we encounter a number we need to update the running number
        # whenever we encounter an opening brace that signals that our running number is fully generated
        # and we need to call the recursive function on the braces as needed
        # 

        stack = []
        for i in range(len(s)):
            curr = s[i]
            # consider curr
            # if the character is not ], we need to push it onto the stack
            # if it is ], that means we need to compute a substring
            # that means we must build the substring and compute the multiplier as we pop
            # until we finish reading the multiplier
            if curr == ']':
                # we need to pop the substrings
                substring = ""
                while stack[-1] != '[':
                    # pop the substring and build it
                    substring = stack.pop() + substring
                # pop the opening brace
                stack.pop()
                # compute the number
                multiplier = 0
                ten = 1
                while stack and stack[-1] >= '0' and stack[-1] <= '9':
                    multiplier += int(stack.pop()) * ten
                    ten *= 10
                print(multiplier)
                
                # the number has been computed, we have finished iterating through the current
                # stack frame
                stack.append(substring * multiplier)
            else:
                stack.append(curr)
            







        return "".join(stack)