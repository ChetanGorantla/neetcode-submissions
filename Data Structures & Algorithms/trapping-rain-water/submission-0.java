class Solution {
    public int trap(int[] height) {
        int n = height.length;
        int[] prefix = new int[n];
        int[] suffix = new int[n];
        int prefixmax = 0;
        int suffixmax = 0;
        
        for (int i = 0; i < n; i++){
            if (height[i] > prefixmax){
                prefixmax = height[i];
            }
            prefix[i] = prefixmax;
        }
        System.out.println(Arrays.toString(prefix));
        for (int i = n-1; i >= 0; i--){
            if (height[i] > suffixmax){
                suffixmax = height[i];
            }
            suffix[i] = suffixmax;
        }
        System.out.println(Arrays.toString(suffix));

        int sum = 0;
        for (int i = 0; i < n; i++){
            sum+=Math.min(suffix[i], prefix[i])-height[i];
        }
        return sum;
    }
}
