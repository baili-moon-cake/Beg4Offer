from functools import lru_cache
class Solution:
    def numTrees(self, n: int):
        return  self.core_func(1,n+1)
    # @lru_cache(maxsize=2**10)
    def core_func(self, begin, end):
        if begin == end:
            return 1
        cnts = 0
        for root_value in range(begin, end):
            cnts+=self.core_func(begin,root_value)*self.core_func(root_value+1,end)
        return cnts
if __name__ == "__main__":
    import timeit
    # sol = Solution()
    # ans = sol.numTrees(3)
    print(timeit.timeit("sol.numTrees(50)", setup="from __main__ import Solution;sol=Solution()",number=10))
    # print(ans)
