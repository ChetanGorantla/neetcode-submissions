class Solution {
    public int search(int[] nums, int target) {
        int l = 0;
        int r = nums.length - 1;

        if (nums.length == 2){
            if (target == nums[0]){
                return 0;
            }else if (target == nums[1]){
                return 1;
            }else{
                return -1;
            }
        }
        while (l < r) {
            int m = l + (r - l) / 2;
            if (nums[m] < nums[r]) {
                r = m;
            } else {
                l = m + 1;
            }
        }
        
        int pivot = l;
        System.out.println(l);
        l = 0;
        r = nums.length-1;
        if (target < nums[r]){
            l = pivot;
        }else if (target > nums[r]){
            r = pivot-1;
        }else{
            return r;
        }

        while (l <= r){
            int mid = (l+r+1)/2;

            if (target > nums[mid]){
                l = mid+1;

            }else if (target < nums[mid]){
                r = mid-1;
            }else{
                return mid;
            }

        }
        return -1;

    }
}
