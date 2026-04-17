class Solution {
    public int reverse(int x) {
        int res = 0;
        int INT_MAX = (int)Math.pow(2, 31) - 1;
        int INT_MIN = -1 * (int)Math.pow(2, 31);
        while (Math.abs(x) > 0){
            // Digits remaining to append but no remaining digit space
            if (res > INT_MAX/10){
                return 0;
            }
            if (res < INT_MIN / 10){
                return 0;
            }
            int curr = x % 10;
            x = (int)(x/10);
            // Last digit to append will exceed bounds
            if (res == (int)(INT_MAX/10) && curr > INT_MAX % 10){
                return 0;
            }
            if (res == (int)(INT_MIN/10) && curr < INT_MIN % 10){
                return 0;
            }
            System.out.println(x);
            System.out.println(res);
            res *= 10;
            res += curr;
        }

        return res;
    }
}
