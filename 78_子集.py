
class Solution:
    def subsets(self, nums):
        return self.look_back_func(nums, 0)
    def look_back_func(self, nums, begin_index):
        if begin_index == len(nums):
            return [[],]
        ret = []
        _subsets = self.look_back_func(nums, begin_index+1)
        for _subset in  _subsets:
            ret.append(list(_subset))
            _subset.append(nums[begin_index])
            ret.append(_subset)
        if ret == []:
            ret = [[],]
        return ret

if __name__ == "__main__":
    sol = Solution()
    print(sol.subsets([1,2,3]))