class Solution:
    def rob(self, nums: List[int]):
        length = len(nums)
        if length == 0:
            return 0
        elif length <= 2:
            return max(nums)
        dp = [0,]*length
        stolen = [False,] *length
        dp[0], stolen[1] = nums[0], nums[1]>nums[0]
        dp[1] = nums[1] if stolen[1] else nums[0]
        for idx in range(2,length):
            if stolen[idx-1]:
                dp[idx] = max(dp[idx-2] + nums[idx], dp[idx-1])
                stolen[idx] = True if dp[idx] > dp[idx-1] else False
            else:
                dp[idx] = dp[idx-1] + nums[idx]
                stolen[idx] = True
        return dp[-1]
