from collections import deque
class Solution:
    def climbStairs(self, n: int):
        if n==1:
            return 1
        elif n==2:
            return 2
        dp = deque(maxlen=3)
        dp.extend([1,2])
        for i in range(2,n):
            dp.append(dp[i-1]+dp[i-2])
        return dp.pop()
