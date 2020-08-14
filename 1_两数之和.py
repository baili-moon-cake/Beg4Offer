class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dic={}
        for k,v in enumerate(nums):
            if target-v in dic: #写之前判断，避免了重复元素的覆盖
                return [dic[target-v],k]
            dic[v]=k