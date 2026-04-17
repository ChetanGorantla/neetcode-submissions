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
                    if (!out.contains(currarr)){
                        out.add(currarr);
                    }
                    //now where to shift l and r now that met a match?
                    //find the direction that produces the least shift?
                    int distance = 0;
                    if (l < nums.length-1 && r > 0){
                        int distl = Math.abs(nums[l+1]-nums[l]);
                        int distr = Math.abs(nums[r]-nums[r-1]);
                        if (distl < distr){
                            l++;
                        }else{
                            r--;
                        }
                        
                    }
                    
                }
            }
            
            

        }
        return out;
    }
}
