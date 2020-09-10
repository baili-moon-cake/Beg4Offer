class Solution:
    def findLengthOfLCIS(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0
        dp = [1 for _ in nums]
        for idx, num in enumerate(nums[1:]):
            dp[idx+1] = dp[idx]+1 if num>nums[idx] else 1
        return max(dp)