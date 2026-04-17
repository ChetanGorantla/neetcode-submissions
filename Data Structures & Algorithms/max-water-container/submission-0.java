class Solution {
    public int maxArea(int[] heights) {
        int l = 0;
        int r = heights.length-1;
        int water = 0;
        for (int i = 0; i < heights.length-1; i++){
            int min = (heights[l] < heights[r] ? l:r);
            int tempwater = heights[min] * (r-l);
            water = Math.max(tempwater, water);
            if (min == l){
                l++;
            }else{
                r--;
            }
            System.out.println(min + "*" + (r-l) + "=" + tempwater);
        }
        return water;
    }
}
