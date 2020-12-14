from typing import List

from collections import deque
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        if k == 1:
            return nums
        ret = [0 for _ in range(len(nums)-k+1)]
        q = deque([nums[0],])
        for idx in range(1,k):
            while(q and q[-1]<nums[idx]):
                q.pop()
            q.append(nums[idx])
        ret[0] = q[0]
        for idx in range(k, len(nums)):
            if q[0] == nums[idx-k]:
                q.popleft()
            while(q and q[-1]<nums[idx]):
                q.pop()
            q.append(nums[idx])
            ret[idx-k+1] = q[0]
        return ret

sol = Solution()
inp = [9,10,9,-7,-4,-8,2,-6]
ans = sol.maxSlidingWindow(inp, k=5)
print(ans)