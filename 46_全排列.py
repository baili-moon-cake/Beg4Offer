class Solution:
    def permute(self, nums):
        unused_set = set(nums)
        return self.permuteRecursively(unused_set)

    def permuteRecursively(self, unused_set):
        if len(unused_set) == 0:
            return [[],]
        ret = []
        nums = set(unused_set)
        for num in nums:
            unused_set.remove(num)
            previous_ret = self.permuteRecursively(unused_set)
            for _ret in previous_ret:
                ret.append(_ret+[num,])
            unused_set.add(num)
        return ret
