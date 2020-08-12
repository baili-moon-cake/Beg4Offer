class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        length = len(nums)
        for idx in range(length):
            while(nums[nums[idx]-1] != nums[idx]):
                curNum = nums[idx]
                nums[idx], nums[curNum-1] = nums[curNum-1], nums[idx]
        missNum_list = []
        for idx, num in enumerate(nums):
            if idx != num -1:
                missNum_list.append(idx+1)
        return missNum_list
