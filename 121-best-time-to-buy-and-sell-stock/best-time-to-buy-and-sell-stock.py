class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        
        # at the beginning the minimum price is the first price
        buy_price = prices[0]

        #  at the beginning the minimum  profit is zero
        profit = 0
        current_profit= 0

        for i in range(1,len(prices)):

            if buy_price > prices[i] :
                buy_price = prices[i]
            else: 
                current_profit = prices[i]-buy_price
                profit = max(current_profit, profit)
        
            
        return profit

