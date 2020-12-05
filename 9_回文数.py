import math
class Solution:
    def isPalindrome(self, x: int) -> bool:
        x = str(x)
        length = len(x)
        for idx in range(math.ceil(length/2)):
            if x[idx] != x[length-1-idx]:
                return False
        return True
sol = Solution()
ans = sol.isPalindrome(66)
print(ans)