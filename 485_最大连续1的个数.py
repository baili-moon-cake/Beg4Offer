from typing import List

class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        consecutive_one_cnt, max_consecutive_one_cnt = 0, 0
        for num in nums:
            if num == 1:
                consecutive_one_cnt += 1
            elif num == 0:
                consecutive_one_cnt = 0
            max_consecutive_one_cnt = max(consecutive_one_cnt, max_consecutive_one_cnt)
        return  max_consecutive_one_cnt


sol = Solution()
nums = [0,0,0,0,0,0]
ans = sol.findMaxConsecutiveOnes(nums)
print(ans)