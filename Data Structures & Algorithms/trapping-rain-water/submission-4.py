class Solution:
    def trap(self, height: List[int]) -> int:
        water = 0
        l = 0
        r = len(height)-1
        lmax = height[l]
        rmax = height[r]

        while l < r:
            # determine which direction to move
            if lmax < rmax:
                # we need to shift l
                l+=1
                lmax = max(lmax, height[l])
                water += lmax - height[l]
            else:
                r-=1
                rmax = max(rmax, height[r])
                water += rmax-height[r]
        return water
        