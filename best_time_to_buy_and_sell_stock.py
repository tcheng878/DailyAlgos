class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        if len(prices) <= 1:
            return 0
        
        Min, Max = prices[0], prices[0]
        output = 0
        
        for i in prices:
            if i < Min:
                Min, Max = i, i
            elif i > Max:
                Max = i
                if Max - Min > output:
                    output = Max - Min
        return output