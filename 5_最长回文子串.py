class Solution:
    def longestPalindrome(self, s: str) -> str:
        if len(s) <= 1:
            return s
        elif len(s) == 2  and s[0] == s[1]:
            return s
        dp = [[False for _ in s] for _ in s]
        for idx in range(len(s)):
            dp[idx][idx] = True
        maxLength = (0,0)
        for i in range(len(s))[::-1]:
            for j in range(len(s)):
                if i>=j: continue
                dp[i][j] = dp[i+1][j-1] and s[i] == s[j] if j-i>1 else s[i]==s[j]
                maxLength = (i,j) if dp[i][j] and j-i>=maxLength[1]-maxLength[0] else maxLength
        return s[maxLength[0]:maxLength[1]+1]



                
