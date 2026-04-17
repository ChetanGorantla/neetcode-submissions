class Solution {
    public int[] productExceptSelf(int[] nums) {
        int[] pre = new int[nums.length];
        int[] post = new int[nums.length];
        int[] out = new int[nums.length];

        //assigning prefixes
        int premult = 1;
        for (int i = 0; i < nums.length; i++){
            premult *= nums[i];
            pre[i] = premult;
        }
        //assigning postfixes
        int postmult = 1;
        for (int i = nums.length-1; i >= 0; i--){
            postmult *= nums[i];
            post[i] = postmult;
        }
        out[0] = post[1];
        out[out.length-1] = pre[out.length-2];

        for (int i = 1; i < nums.length-1; i++){
            
            out[i] = pre[i-1] * post[i+1];
        }
        return out;
    }
}  
