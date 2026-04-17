class Solution {
    public int maxProfit(int[] prices) {
        int l = 0;
        int r = 1;
        int maxprofit = 0;
        while (l < r && r < prices.length){
            int curr = prices[r]-prices[l];
            if (curr >= 0){
                maxprofit = Math.max(maxprofit, curr);
                r++;
            }else{
                
                l++;
                r=l+1;
            }
            
        }
        return maxprofit;
    }
}
