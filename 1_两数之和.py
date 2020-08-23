class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        if len(nums)<2:
            return []
        dic={}
        for idx,v in enumerate(nums):
            dic[v]=dic.setdefault(v,[])+[idx,]
        for idx,v in enumerate(nums):
            if target-v in dic:
                if v == target-v:
                    if len(dic[v])==2:
                        return dic[v]
                    else:
                        continue
                else:
                    return [idx,dic[target-v][-1]]
        return []