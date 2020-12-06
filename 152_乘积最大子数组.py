from typing import List


class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        dp_max = [nums[0] for _ in nums]
        dp_min = [nums[0] for _ in nums]
        max_product = nums[0]
        for idx in range(1, len(nums)):
            tmp_max = max(
                dp_max[idx-1]*nums[idx],
                dp_min[idx-1]*nums[idx],
                nums[idx])
            if tmp_max > max_product:
                max_product = tmp_max
            dp_max[idx] = max(dp_max[idx-1]*nums[idx], dp_min[idx-1]*nums[idx], nums[idx])
            dp_min[idx] = min(dp_min[idx-1]*nums[idx], dp_max[idx-1]*nums[idx], nums[idx])
        return max_product


sol = Solution()
inp = [1,2,-9,6]
ans = sol.maxProduct(inp)
print(ans)