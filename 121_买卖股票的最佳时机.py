class Solution:
    def maxProfit(self, prices: List[int]):
        if not prices:
            return 0
        maxProfit = float('-inf')
        curProfit = 0
        buyPrice = float('inf')
        for price in prices:
            if price < buyPrice:
                buyPrice=price
            else:
                curProfit = price - buyPrice
            maxProfit = curProfit if curProfit>maxProfit else maxProfit 
        return maxProfit
