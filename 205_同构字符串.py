class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        hashmap = {}
        used = set()
        for s_char, t_char in zip(s,t):
            if s_char in hashmap:
                if t_char != hashmap[s_char]:
                    return False
            else:
                if t_char in used:
                    return False
                else:
                    used.add(t_char)
                hashmap[s_char] = t_char
        return True


sol = Solution()
s = "aab";t = "aaa"
ans = sol.isIsomorphic(s, t)
print(ans)