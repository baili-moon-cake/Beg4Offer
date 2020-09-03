class Solution:
    def canJump(self, nums: List[int]):
        if len(nums)==1:
            return True
        dp = [-1 for _ in range(len(nums))]
        dp[0] = nums[0]
        for idx in range(1,len(nums)):
            if dp[idx-1] >= 1:
                dp[idx] = max(dp[idx-1]-1, nums[idx])
        return  dp[-1] >= 0
