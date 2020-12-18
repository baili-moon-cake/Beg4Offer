from collections import Counter

class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        hashmap = Counter(t)
        for char in s:
            hashmap[char] -= 1
            if hashmap[char] == 0:
                hashmap.pop(char)
        return list(hashmap.keys())[0]

sol = Solution()
s = "ae"
t = "aea"
ans = sol.findTheDifference(s, t)
print(ans)