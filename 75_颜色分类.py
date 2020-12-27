from typing import List

class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        head_idx, tail_idx = 0, len(nums)-1
        for idx, n in enumerate(nums):
            while(nums[idx]!=1 and tail_idx>=idx>=head_idx):
                if nums[idx] == 0:
                    nums[head_idx], nums[idx] =  nums[idx], nums[head_idx]
                    head_idx += 1
                elif nums[idx] == 2:
                    nums[tail_idx], nums[idx] =  nums[idx], nums[tail_idx]
                    tail_idx -= 1


sol = Solution()
inp =  [2,2,2,1,1,2,0,2,0,1,1,0,0,0]
sol.sortColors(inp)
print(inp)