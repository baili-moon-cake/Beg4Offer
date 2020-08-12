class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        if not nums:
            return
        cntOfZero = nums.count(0)
        if not cntOfZero:
            return 
        length = len(nums)
        idxOfNonZero = 0
        for idx, num in enumerate(nums):
            if num:
                nums[idxOfNonZero]=num
                idxOfNonZero += 1
                if idx >= length-cntOfZero:
                    nums[idx] = 0
            else:
                continue
            