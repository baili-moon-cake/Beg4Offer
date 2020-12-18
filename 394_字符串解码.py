from collections import deque

class Solution:
    def decodeString(self, s: str) -> str:
        string_q = deque(['',])
        multipler_q = deque([1,])
        multipler = 0
        for char in s:
            if char.isdigit():
                multipler = multipler * 10 + int(char)
            elif char == '[':
                multipler_q.append(multipler)
                multipler = 0
                string_q.append('')
            elif char == ']':
                tmp_str = string_q.pop()
                string_q[-1] += multipler_q[-1] * tmp_str
                multipler_q.pop()
            else:
                string_q[-1] += char
        return string_q[0]

sol = Solution()
s = "abc3[cd]xyz"
ans = sol.decodeString(s)
print(ans)