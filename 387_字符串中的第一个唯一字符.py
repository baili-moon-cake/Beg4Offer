from collections import OrderedDict

class Solution:
    def firstUniqChar(self, s: str) -> int:
        hashmap = OrderedDict()
        for char in s:
            hashmap[char] = hashmap.setdefault(char, 0) + 1
        for k in hashmap.keys():
            if hashmap[k] == 1:
                return s.index(k)
        else:
            return -1

sol = Solution()
s = 'loveleetcode'
ans = sol.firstUniqChar(s)
print(ans)