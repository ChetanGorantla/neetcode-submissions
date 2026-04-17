class Solution {
    public int[] sortedSquares(int[] nums) {
        //start from ends, compare and decrement as needed
        int l = 0; int r = nums.length - 1;
        int idx = nums.length-1;
        int[] out = new int[nums.length];
        while (l <= r){
            if (Math.abs(nums[l]) > Math.abs(nums[r])){
                out[idx] = (int)Math.pow(nums[l],2);
                l++;
            }else{
                out[idx] = (int)Math.pow(nums[r],2);
                r--;
            }
            idx--;
        }
        return out;
    }
}