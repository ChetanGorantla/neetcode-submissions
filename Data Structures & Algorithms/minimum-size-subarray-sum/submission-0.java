class Solution {
    public int minSubArrayLen(int target, int[] nums) {
        int l = 0;
        int r = 0;
        int currsum = 0;
        int len = 0;
        int minlen = Integer.MAX_VALUE;
        while (l <= r && r < nums.length){
            currsum+=nums[r];
            if (currsum >= target){
                minlen = Math.min(minlen, r-l+1);
                currsum=0;
                l++;
                r = l;
                
            }else{
                r++;
            }
        }
        if (minlen == Integer.MAX_VALUE){
            minlen = 0;
        }
        return minlen;
    }
}