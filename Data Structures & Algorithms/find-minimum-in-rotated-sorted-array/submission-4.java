class Solution {
    public int findMin(int[] nums) {
        //always exhibits +-1 behavior unless its a break point, and then return the second break pt
        //r-l != 1

        int l = 0;
        int r = nums.length-1;
        int ans = 0;
        if (nums.length == 1){
            return nums[0];
        }else if (nums.length == 2){
            return Math.min(nums[0], nums[1]);
        }
        while (l < r){
            int mid = (r+l+1)/2;
            if (r-l == 1){
                ans = nums[r];
                break;
            }
            int diff1 = Math.abs(nums[r] - nums[l]);
            int diff2 = Math.abs(nums[r] - nums[mid]);
            int diff3 = Math.abs(nums[mid]-nums[l]);
            int highestdiff = Math.max(Math.max(diff1, diff2), diff3);

            if (highestdiff == diff2){
                l = mid;
            }else if (highestdiff == diff3){
                r = mid;
            }else if (highestdiff == diff1){
                ans = nums[l];
                break;
            }

            System.out.println("shifting to " + l + " " + r);
            

        }
        return ans;
    }
}
