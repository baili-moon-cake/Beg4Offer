from collections import Counter, deque

class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        remains_record = Counter(s)
        stack = deque()
        seen = set()
        for char in s: 
            remains_record[char] -= 1
            if char not in seen:
                while(stack and stack[-1]>char and remains_record[stack[-1]]>0):
                    seen.discard(stack.pop())
                seen.add(char)
                stack.append(char)
        return ''.join(stack)

sol = Solution()
s = "cbacdcbc"
ans = sol.removeDuplicateLetters(s)
print(ans)