from typing import List


# # 使用最小堆来完成
# class Solution:
#     def findKthLargest(self, nums: List[int], k: int) -> int:
#         self.min_heap = [-float('inf')] * k
#         self.k = k
#         for num in nums:
#             if num > self.min_heap[0]:
#                 self.min_heap[0] = num
#                 self.siftdown(0)
#         return self.min_heap[0]

#     def siftdown(self, idx):
#         next_idx = None
#         if 2*idx+1 < self.k:
#             next_idx = 2 * idx + 1
#         if 2*idx+2 < self.k:
#             next_idx = 2*idx+2 \
#                 if self.min_heap[2*idx+2]<self.min_heap[2*idx+1] \
#                 else next_idx
#         if next_idx and self.min_heap[idx] > self.min_heap[next_idx]:
#             self.min_heap[idx], self.min_heap[next_idx] = \
#                 self.min_heap[next_idx], self.min_heap[idx]
#             self.siftdown(next_idx)


# 快速排序
import random
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        left, right = 0, len(nums)-1
        target_idx = len(nums) - k
        sure_pos = self.swap(nums, left, right)
        while(sure_pos != target_idx):
            if sure_pos > target_idx:
                right = sure_pos - 1
                sure_pos = self.swap(nums, left, right)
            else:
                left = sure_pos + 1
                sure_pos = self.swap(nums, left, right)
        return nums[sure_pos]

    def swap(self, nums, left, right):
        pivot_idx = random.randint(left, right)
        pivot = nums[pivot_idx]
        nums[right], nums[pivot_idx] = nums[pivot_idx], nums[right]
        pos = left
        for idx in range(left, right):
            if nums[idx] < pivot:
                nums[idx], nums[pos] = nums[pos], nums[idx]
                pos += 1
        nums[right], nums[pos] = nums[pos], nums[right]
        return pos

sol = Solution()
ans = sol.findKthLargest([99,99], 1)
print(ans)