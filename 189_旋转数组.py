from typing import List

class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        length = len(nums)
        if length<=1 or k==0:
            return nums
        k %= length
        self.reverse(nums, 0, length-k-1)
        self.reverse(nums, length-k, length-1)
        self.reverse(nums, 0, length-1)
        return nums
    def reverse(self, _list, l_idx, r_idx):
        while(l_idx<r_idx):
            _list[l_idx], _list[r_idx] = _list[r_idx], _list[l_idx]
            l_idx += 1
            r_idx -= 1
            


sol = Solution()
inp = [1,2,3,4,5,6,7];k = 1
ans = sol.rotate(inp, k)
print(ans)