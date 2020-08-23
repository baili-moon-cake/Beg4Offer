import collections
class Solution:
    def isValid(self, s: str) -> bool:
        stack = collections.deque()
        LookupTable = {')':'(',']':'[','}':'{'}
        for char in s:
            if char in ['(','[','{']:
                stack.append(char)
            elif char in LookupTable:
                if len(stack)>0 and LookupTable[char]==stack.pop():
                    continue
                else:
                    return False
        return len(stack)==0

