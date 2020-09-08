import bisect
class Solution:
    def lengthOfLIS(self, nums):
        if len(nums) == 0:
            return 0
        dp = [nums[0],]
        for num in nums[1:]:
            self.update_dp(dp, num)
        return len(dp)
    def update_dp(self, dp, target):
        insert_index = bisect.bisect_left(dp,target)
        if insert_index == len(dp):
            insert_index -= 1
            dp.append(target)
        else:
            dp[insert_index] = target

if __name__ == "__main__":
    sol = Solution()
    ans = sol.lengthOfLIS([9,7,6,3,2,1])
    print(ans)