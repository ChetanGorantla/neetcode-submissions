class Solution {
    public int minEatingSpeed(int[] piles, int h) {
        
        int l = 1;
        int r = Arrays.stream(piles).max().getAsInt();
        int res = 0;
        //rates list is defined
        while (l <= r){
            int k = (l+r)/2;
            long totalTime = 0;
            for (int pile: piles){
                totalTime += Math.ceil((double) pile/k);
            }
            if (totalTime > h){
                l = k+1;
            }else{
                res = k;
                r = k-1;
            }
        }
        return res;
    }
}
