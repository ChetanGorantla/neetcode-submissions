class Solution {
    public boolean containsNearbyDuplicate(int[] nums, int k) {
        int l = 0;
        int r = 1;
        while (r < nums.length){
            if (nums[l] == nums[r]){
                if (r-l <= k){
                    System.out.println("r:"+r + "l:"+l);
                    return true;
                }
            }else{
                if (r-l == k){
                    l++;
                    if (l == r){
                        r++;
                    }
                }else if (l == r-1){
                    r++;
                }else{
                    r++;
                }
            }
        }
        return false;
    }
}