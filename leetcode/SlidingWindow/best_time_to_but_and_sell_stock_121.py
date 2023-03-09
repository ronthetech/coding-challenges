from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l,r=0,1 # left=buy, right=sell
        maxP = 0

        while r < len(prices):
            # is it a profitable transaction?
            if prices[l] < prices[r]:
                profit = prices[r] - prices[l]
                maxP = max(maxP, profit)
            else:
                l=r
            r=r+1
        return maxP
    
    def maxProfit2(self, prices: List[int]) -> int:
        res = []
        
        lowest = prices[0]
        for price in prices:
            if price < lowest:
                lowest = price
            res = max(res, price-lowest)
        return res
      