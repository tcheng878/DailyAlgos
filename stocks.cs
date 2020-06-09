public class Solution {
    public int MaxProfit(int[] prices) {
        if(prices.Length <= 1){
            return 0;
        }
        int small = prices[0];
        int large = prices[0];
        int profit = 0;
        
        for(int i = 0; i < prices.Length; i++){
            if(prices[i] < small){
                small = prices[i];
                large = prices[i];
            }
            else if(prices[i] > large){
                large = prices[i];
                if((large - small) > profit){
                    profit = large - small;
                }
            }
            // Console.WriteLine("large" + large);
            // Console.WriteLine("small" + small);
        }
        return profit;
    }
}