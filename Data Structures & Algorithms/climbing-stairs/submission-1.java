class Solution {
    public int climbStairs(int n) {
        int one = 0;
        int two = 1;
        for (int i = 0; i < n; i++){
            int temp = one;
            one = two;
            two = one+temp;
        }
        return two;
    }
}
