from typing import List

import bisect
class Solution:
    def reversePairs(self, nums: List[int]) -> int:
        keep_sorted_list = []
        cnts = 0
        for num in nums[::-1]:
            cnts += bisect.bisect_left(keep_sorted_list, num)
            keep_sorted_list.insert(
                bisect.bisect_left(keep_sorted_list, 2*num),\
                2*num)
        return cnts

sol = Solution()
inp = [1,3,2,3,1]
ans = sol.reversePairs(inp)
print(ans)