class Solution {
    public int search(int[] nums, int target) {
        int l = 0;
        int r = nums.length-1;
        
        while (l <= r){
            int mid = (int)((l+r)/2);
            System.out.println("Current index at " + mid);
            if (nums[mid] < target){
                l = mid+1;
            }else if (nums[mid] > target){
                r = mid-1;
            }else if (nums[mid] == target){
                return mid;
            }
        }
        return -1;
    }
}
