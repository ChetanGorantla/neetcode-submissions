class Solution {
    public List<List<Integer>> threeSum(int[] nums) {
        Arrays.sort(nums);
        System.out.println(Arrays.toString(nums));
        List<List<Integer>> out = new ArrayList<>();
        for (int i = 0; i < nums.length; i++){
            if (nums[i] > 0){
                break;
            }
            if (i > 0 && nums[i] == nums[i-1]){
                continue;
            }
            int curr = -1 * (nums[i]);
            int l = i+1; int r = nums.length-1;
            boolean passed = false;
            System.out.println("looking to sum " + curr);
            while (l < r){
                System.out.println("left " + l + " right " + r);
                int sum = nums[l] + nums[r];
                System.out.println("current sum " + sum);
                if (sum < curr){
                    l++;
                }else if (sum > curr){
                    r--;
                }else if (sum == curr){
                    passed = true;
                    List<Integer> currarr = new ArrayList<>();
                    currarr.add(nums[i]);
                    currarr.add(nums[l]);
                    currarr.add(nums[r]);
                    out.add(currarr);
                    //now where to shift l and r now that met a match?
                    //find the direction that produces the least shift?
                    //or just keep shifting l++ if your next l values are the same
                    //^ because we just need to skip whatever repeats
                    //^ and then continue the loop to find the matches.
                    //^ we aren't breaking and reentering, we're staying in loop

                    //instead of finding minimum direction to shift, we can simply shift both
                    //this is because there's no way we can shift one direction and -
                    // - keep the other the same and attempt to achieve the same sum.
                    // ^ unless there's duplicates, which we skip.
                    // We have to shift both.
                    l++;
                    r--;
                    while (l < r && nums[l] == nums[l-1]){
                        l++;
                    }
                    
                }
            }
            
            

        }
        return out;
    }
}
