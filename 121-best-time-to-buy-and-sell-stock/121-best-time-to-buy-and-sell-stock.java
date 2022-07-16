class Solution {
    public int maxProfit(int[] prices) {
        int l = 0;
        int ans = 0;
        for(int r=1; r<prices.length;r++){
            int profit = prices[r] - prices[l];
            ans = Math.max(ans, profit);
            if (prices[r]< prices[l]){
                l =r;
            }
        }
        return ans;
    }
}