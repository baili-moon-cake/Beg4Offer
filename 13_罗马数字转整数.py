class Solution:
    digit_lookuptable = {
        'I':1, 'V':5,
        'X':10, 'L':50,
        'C':100, 'D':500,
        'M':1000
    }               
    def romanToInt(self, s: str) -> int:
        ret, skip, length = 0, False, len(s)
        for idx in range(length):
            if skip:
                skip = False
                continue
            if idx != length - 1 and \
              self.digit_lookuptable[s[idx]] < \
              self.digit_lookuptable[s[idx+1]]:
                ret += self.digit_lookuptable[s[idx+1]] - \
                    self.digit_lookuptable[s[idx]]
                skip = True
            else:
                ret += self.digit_lookuptable[s[idx]]
        return ret


sol = Solution()
ans = sol.romanToInt('LVIII')
print(ans)