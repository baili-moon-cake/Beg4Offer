from typing import List


class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        length = len(nums)
        if length <= 1:
            return nums
        length_limit = length // 3
        candidate1 = [nums[0], 1]
        candidate2 = [None, 0]
        for start_idx, num in enumerate(nums[1:], start=1):
            if num == candidate1[0]:
                candidate1[1] += 1
            else:
                candidate2[0], candidate2[1] = [num, 1]
                break
        for idx in range(start_idx+1, length):
            if nums[idx] == candidate1[0]:
                candidate1[1] += 1
            elif nums[idx] == candidate2[0]:
                candidate2[1] += 1
            else:
                if candidate1[1] == 0:
                    candidate1[0], candidate1[1] = nums[idx], 1
                    continue
                if candidate2[1] == 0:
                    candidate2[0], candidate2[1] = nums[idx], 1
                    continue
                candidate1[1] -= 1
                candidate2[1] -= 1

        ret = [
            candidate for candidate, cnts in [candidate1,candidate2] 
            if cnts >0 and nums.count(candidate) > length_limit
        ]
        return ret


sol = Solution()
inp = [4,2,1,1]
ans = sol.majorityElement(inp)
print(ans)