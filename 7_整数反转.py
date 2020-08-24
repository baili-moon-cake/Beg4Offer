class Solution:
    def reverse(self, x: int) -> int:
        if abs(x) > 2**31-1:
            return 0
        ret = int(str(abs(x))[::-1]) if x>=0 else -int(str(abs(x))[::-1]) 
        return ret if abs(ret) <2**31-1 else 0 