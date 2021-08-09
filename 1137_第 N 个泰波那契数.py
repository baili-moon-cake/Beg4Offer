# from Typing import int


class Solution:
    def tribonacci(self, n: int) -> int:
        if n == 0:
            return 0
        elif n == 1:
            return 1
        elif n == 2:
            return 1
        a, b, c = 0, 1, 1

        for idx in range(n-2):
            a, b, c = b, c, a + b + c
        return c

sol = Solution()
ans = sol.tribonacci(25)
print(ans)