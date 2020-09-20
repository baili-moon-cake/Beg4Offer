class Solution:
    def myPow(self, x: float, n: int) -> float:
        if x == 0:
            return 0
        elif n==0:
            return 1
        if n<0:
            return self.corefunc(1/x,-n)
        return self.corefunc(x,n)
    def corefunc(self, x, n):
        if n==0:
            return 1
        elif n==1:
            return x
        divisor, remainder = divmod(n,2)
        if remainder:
            return (self.corefunc(x, divisor)**2)*x
        return self.corefunc(x, n//2)**2

    def naive_implement(self, x, n):
        if n<0:
            x,n = 1/x,-n
        return x**n


if __name__ == "__main__":
    import timeit
    # sol = Solution()
    # ans = sol.numTrees(3)
    print(timeit.timeit("sol.myPow(2,2**31-1)", setup="from __main__ import Solution;sol=Solution()",number=10))
    print(timeit.timeit("sol.naive_implement(2,2**31-1)", setup="from __main__ import Solution;sol=Solution()",number=10))
    
    # print(ans)