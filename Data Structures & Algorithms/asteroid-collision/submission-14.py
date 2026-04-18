class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack = []
        for a in asteroids:
            while stack and a < 0 and stack[-1] > 0:
                diff = a + stack[-1]
                if diff < 0:
                    # continue condition, break down the front
                    stack.pop()
                elif diff > 0:
                    # break condition, no further change
                    a = 0
                else:
                    # break condition, equality
                    a = 0
                    stack.pop()
            # if we have a valid incoming asteroid to continue the path, add it
            if a:
                stack.append(a)
        return stack

        
        
            