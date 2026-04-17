class Solution {
    public int[] getConcatenation(int[] nums) {
        int[] out = new int[nums.length * 2];
        for (int i = 0; i < nums.length; i++){
            out[i] = nums[i];
            out[i+nums.length] = nums[i];
        }
        return out;
    }
}