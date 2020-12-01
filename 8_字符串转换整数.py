class Solution:
    def myAtoi(self, s: str) -> int:
        s = s.strip(' ')
        if s == '':
            return 0
        elif s[0] == '+':
            signal = 1
            s = s[1:]
        elif s[0] == '-':
            signal = -1
            s = s[1:]
        elif '0'<= s[0] <='9':
            signal = 1
        else:
            return 0
        digits = ''
        for char in s:
            if '0' <= char <= '9':
                digits += char
            else:
                break
        if digits == '':
            return 0
        digits = int(digits) * signal
        if digits > 2 ** 31 - 1:
            return 2 ** 31 - 1
        elif digits <  -2 ** 31:
            return -2 ** 31
        else:
            return digits

sol = Solution()
ans = sol.myAtoi('-91283472332')
print(ans)