import numpy as np
# [3,3,5,0,0,3,1,4]
class Solution:
    def maxProfit(self, prices: List[int]):
        length = len(prices)
        if length<=0:
            return 0
        dp = np.zeros((length,3,2))
        dp[0,:,:]=0
        dp[:,0,:]=0
        dp[0,1:,1]=-prices[0]
        for day in range(1, length):
            for k in range(1,3):
                dp[day,k,0]=max(dp[day-1,k,0],dp[day-1,k,1]+prices[day])
                dp[day,k,1]=max(dp[day-1,k,1],dp[day-1,k-1,0]-prices[day])
        return int(dp[-1,2,0])
