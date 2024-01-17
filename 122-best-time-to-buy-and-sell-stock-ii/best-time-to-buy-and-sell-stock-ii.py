class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """

    #    I have seen a lot of solutions finding the best subarray, but the problem really boils down to wether the price is increasing or decreasing day over day. For example, if the prices are [1, 2, 3, 4, 5]. Solving for the max profit by buying on Day 1 at 1andsellingonDay5 at1 and selling on Day 5 at 1 and sellingon Day5 at 5 for a profit of 4isthesameasbuyingandsellingeveryday(4 is the same as buying and selling every day (4isthesameasbuyingandsellingeveryday(2-1+1 +1+3 - 2+2 +2+4 - 3+3 +3+5 -$4). For cases when the price goes down, there is no reason to track the price as it will either increase on the next iteration (in which case it will be added) or it will continue going down. Hope this helps!
        
        # Start with index 1 and compare the price 
        # with previous day price to calculate profit if any

        total = 0
        for i in range(1,len(prices)):
            if prices[i] > prices[i-1]:
                total += (prices[i]-prices[i-1])
        
        return total
   