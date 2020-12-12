from typing import List

class Solution:
    def wiggleMaxLength(self, nums: List[int]) -> int:
        nums_length = len(nums)
        if nums_length < 2:
            return nums_length
        dp = [[1,1] for _ in nums]
        max_length = 1
        for idx in range(1, nums_length):
            for i in range(idx):
                if nums[idx] < nums[i]:
                    dp[idx][1] = max(dp[i][0]+1,dp[idx][1])
                elif nums[idx] > nums[i]:
                    dp[idx][0] = max(dp[i][1]+1,dp[idx][0])
                max_length = max(max_length, dp[idx][0], dp[idx][1])
        return max_length



class Solution:
    def wiggleMaxLength(self, nums: List[int]) -> int:
        nums_length = len(nums)
        if nums_length < 2:
            return nums_length
        ascend_num, ascend_length = nums[0], 1
        descend_num, descend_length = nums[0], 1
        for idx in range(1, nums_length):
            tmp_ascend_num, tmp_descend_num = \
                 ascend_num, descend_num
            tmp_ascend_length, tmp_descend_length = \
                 ascend_length, descend_length
            if nums[idx] > descend_num:
                if descend_length+1 > ascend_length:
                    tmp_ascend_length = descend_length + 1
                    tmp_ascend_num = nums[idx]
                elif descend_length+1 == ascend_length:
                    tmp_ascend_num = max(nums[idx], ascend_num)
            if nums[idx] < ascend_num:
                if ascend_length+1 > descend_length:
                    tmp_descend_length = ascend_length + 1
                    tmp_descend_num = nums[idx]
                elif ascend_length+1 == descend_length:
                    tmp_descend_num = min(nums[idx], descend_num)
            ascend_num, descend_num = \
                 tmp_ascend_num, tmp_descend_num
            ascend_length, descend_length = \
                 tmp_ascend_length, tmp_descend_length
        return max(ascend_length, descend_length)



sol = Solution()
inp = [33,53,12,64,50,41,45,21,97,35,47,92,39,0,93,55,40,46,69,42,6,95,51,68,72,9,32,84,34,64,6,2,26,98,3,43,30,60,3,68,82,9,97,19,27,98,99,4,30,96,37,9,78,43,64,4,65,30,84,90,87,64,18,50,60,1,40,32,48,50,76,100,57,29,63,53,46,57,93,98,42,80,82,9,41,55,69,84,82,79,30,79,18,97,67,23,52,38,74,15]
ans = sol.wiggleMaxLength(inp)
print(ans)