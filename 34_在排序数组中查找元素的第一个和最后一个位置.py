import bisect
class Solution:
    def searchRange(self, nums: List[int], target: int):        
        if len(nums) == 0:
            return [-1,-1]
        left_idx = bisect.bisect_left(nums, target)
        right_idx = bisect.bisect_right(nums, target)
        # 没能找到target
        if left_idx>=len(nums) or nums[left_idx] != target:
            return [-1,-1]
        return [left_idx, right_idx-1]