class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        if s == '':
            return p == ''
        elif p == '':
            return False

        slength = len(s)
        plength = len(p)
        sidx, pidx = 0, 0
        star_match_char = None
        while(sidx<slength):
            if pidx >= plength:
                return False
            if s[sidx] == p[pidx] or p[pidx] == '.':
                sidx += 1
                pidx += 1
                star_match_char = None
            elif p[pidx] == '*':
                if p[pidx-1] == '.' or s[sidx] == s[sidx-1]:
                    star_match_char = s[sidx]
                    sidx += 1
                else:
                    pidx += 1
            else:
                if pidx+1 < plength and p[pidx+1] == '*':
                    pidx = pidx+2
                    star_match_char = None
                elif p[pidx] == star_match_char:
                    pidx += 1
                else:
                    return False
        for char in p[pidx:]:
            if char != '*' and char != star_match_char:
                return False
        else:
            return True        
        # if pidx == plength:
        #     return True
        # elif pidx == '*':
        #     return 
        # # else:
        # #     return self.isMatch(s[slength-(plength-pidx-1):], p[pidx:])

sol = Solution()
s = "aaa"; p="a*a"
ans = sol.isMatch(s, p)
print(ans)


