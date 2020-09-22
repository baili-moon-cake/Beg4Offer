from typing import List
class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        if len(nums) <= 1:
            return None
        for idx in range(len(nums)):
            while(nums[idx]!=idx+1):
                src, target = nums[idx], nums[nums[idx]-1]
                if target == src:
                    return src
                nums[idx], nums[src-1] = target, src
sol = Solution()
ans = sol.findDuplicate([2,1,2])
print(ans)