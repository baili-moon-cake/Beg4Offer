from typing import List

import itertools
import operator
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        ret  = list(itertools.accumulate(nums, operator.mul, initial=1))[:-1]
        temp, length = nums[-1], len(nums)
        for idx, num in enumerate(nums[::-1][1:], start=1):
            ret[length-idx-1] *= temp 
            temp *= num
        return ret


sol = Solution()
ans = sol.productExceptSelf([1,2,3,4,7,8,9])
print(ans)
