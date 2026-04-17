class Solution {
    public int[] twoSum(int[] numbers, int target) {
        int l = 0;
        int r = numbers.length-1;
        while (l < r){
            int sum = numbers[l] + numbers[r];
            System.out.println("" + l + r + sum);
            if (sum != target){
                if (sum > target){
                    r--;
                }else{
                    l++;
                }
                /*
                if ((numbers[l] - numbers[l+1]) > (numbers[r] - numbers[r-1])){
                    r--;
                }else{
                    l++;
                }
                continue;
                */
            }else{
                break;
            }
                
            
                
            
        }
        int[] arr = {l+1, r+1};
        return arr;
    }
}
