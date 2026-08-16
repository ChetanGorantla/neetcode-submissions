class Solution:
    def trap(self, height: List[int]) -> int:
        # maintain prefix maximum and suffix maximum
        prefixes = [0] * len(height)
        suffixes = [0] * len(height)
        for i in range(len(height)):
            if i == 0:
                prefixes[i] = height[i]
            else:
                prefixes[i] = max(height[i], prefixes[i-1])
        for i in range(len(height)-1, -1, -1):
            if i == len(height)-1:
                suffixes[i] = height[i]
            else:
                suffixes[i] = max(height[i], suffixes[i+1])
        
        # prefixes and suffixes both built
        # go through the entire array
        #print(prefixes)
        #print(suffixes)
        water = 0
        for i in range(len(height)):
            water += min(prefixes[i], suffixes[i]) - height[i]
        
        return water
        