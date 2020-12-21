from typing import List
from collections import deque


class Solution:
    def maxResult(self, nums: List[int], k: int) -> int:
        dp = deque([(0,nums[0]),]) 
        length = len(nums)
        for idx in range(1,length):
            if dp[0][0] < max(0,idx-k):
                dp.popleft()
            tmp = nums[idx]+dp[0][1]
            while(len(dp)>0 and dp[-1][1]<=tmp):
                dp.pop()
            dp.append((idx, tmp))
        return dp[-1][1]

sol = Solution()
nums = [1,-5,-20,4,-1,3,-6,-3]
k = 2
ans = sol.maxResult(nums, k)
print(ans)