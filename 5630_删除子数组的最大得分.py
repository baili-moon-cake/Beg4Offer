from typing import List

class Solution:
    def maximumUniqueSubarray(self, nums: List[int]) -> int:
        dp_idx = [0 for _ in nums]
        dp_accsum = [0 for _ in nums]
        maxvalue = nums[0]
        dp_accsum[0] = nums[0]
        for r_idx in range(1,len(nums)):
            for _idx in range(dp_idx[r_idx-1],r_idx+1):
                if nums[r_idx] == nums[_idx]:
                    break
            if _idx == r_idx:
                dp_idx[r_idx] = dp_idx[r_idx-1]
            else:
                dp_idx[r_idx] = _idx + 1 
            dp_accsum[r_idx] = dp_accsum[r_idx-1]+nums[r_idx]
            if dp_idx[r_idx] == 0:
                maxvalue = dp_accsum[r_idx]
            else:
                maxvalue = max(maxvalue, dp_accsum[r_idx]-dp_accsum[dp_idx[r_idx]-1])
        return maxvalue

sol = Solution()
inp = [4,4]
ans = sol.maximumUniqueSubarray(inp)
print(ans)