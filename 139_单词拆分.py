from typing import List

class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        import functools
        @functools.lru_cache(None)
        def back_track(s):
            if(not s):
                return True
            res=False
            for i in range(1,len(s)+1):
                if(s[:i] in wordDict):
                    res=back_track(s[i:]) or res
            return res
        return back_track(s)



from collections import deque

class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        if len(wordDict) == 0:
            return False
        q =  deque([s,])
        while(len(q)):
            remain_str = q.popleft()
            if remain_str == '':
                return True
            for idx in range(len(remain_str)+1):
                if remain_str[:idx] in wordDict:
                    q.append(remain_str[idx:])
        return False


sol = Solution()
inp_str = "catsanddog"
inp_wordDict =  ["cats", "dog", "sand", "and", "cat"]
ans = sol.wordBreak(inp_str, inp_wordDict)
print(ans)