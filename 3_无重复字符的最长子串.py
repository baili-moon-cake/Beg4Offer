class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s)<1:
            return 0
        dp = [0 for _ in range(len(s))]
        dp[0] = 1

        for idx in range(1,len(s)):
            newLength = self.getLength(s,idx)
            dp[idx] = max(dp[idx-1],newLength)
        return dp[-1]

    # 在一个字符串中，判断以某个特定字符为结尾的最大无重复字符串的长度
    def getLength(self,s,idx):
        tmpStr=s[idx]
        while(idx>0):
            idx-=1
            if s[idx] not in tmpStr:
                tmpStr+=s[idx]
            else:
                break
        return len(tmpStr) 