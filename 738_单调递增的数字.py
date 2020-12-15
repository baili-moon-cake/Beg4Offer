class Solution:
    def monotoneIncreasingDigits(self, N: int) -> int:
        i = 1
        res = N
        while i <= res/10 :
            n = res // i % 100
            i = i * 10
            if n//10 > n%10 :
                res = res // i * i - 1
        return res