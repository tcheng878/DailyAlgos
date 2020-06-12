class Solution(object):
    def maxProfit(self, prices, fee):
        """
        :type prices: List[int]
        :type fee: int
        :rtype: int
        """
        if len(prices) <= 1:
            return 0
        
        minn, maxx = prices[0], prices[0]
        profit = 0
        flag = False
        
        for i in range(1, len(prices), 1):
            if prices[i] < minn:
                minn = prices[i]
                maxx = prices[i]
                flag = False
            elif prices[i] > maxx:
                maxx = prices[i]
                flag = True
            if flag:
                if i == len(prices) - 1 and maxx > minn + fee:
                    profit += maxx - minn - fee 
                elif i == len(prices) - 1:
                    pass
                elif prices[i + 1] + fee < maxx:
                    profit += maxx - minn - fee
                    maxx = prices[i + 1]
                    minn = prices[i + 1]
                    flag = False
        return profit
            
        