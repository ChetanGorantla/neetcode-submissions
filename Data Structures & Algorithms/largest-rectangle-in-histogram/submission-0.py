class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        maxArea = 0
        stack = [] #pair: (index, height)
        for i,h in enumerate(heights):
            start = i
            while stack and stack[-1][1] > h:#if prev stack height is greater than current height
                index, height = stack.pop()
                maxArea = max(maxArea, height * (i - index))
                start = index
            #now that we are in order of increasing heights, start index is the first instance
            #of the new stack value
            stack.append((start, h))
        for i, h in stack:
            maxArea = max(maxArea, h * (len(heights)-i)) #because heights are extended to end of array
        return maxArea


        