class Solution:
    def maxArea(self, heights: List[int]) -> int:
        # need to converge
        # horizontal shift must be made based on judgement of vertical optimality

        max_area = 0
        l = 0
        r = len(heights)-1

        while (l < r):
            max_area = max(max_area, min(heights[l], heights[r]) * (r-l))
            # you will ALWAYS be limited by the smaller height
            # therefore, you will never locate a larger area if sticking with the smaller height
            # thus, you must always shift the smaller height in search of a better optimum

            if heights[l] < heights[r]:
                l+=1
            else:
                r-=1
            
        return max_area
