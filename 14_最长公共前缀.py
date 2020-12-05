from typing import List

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        prefix = ''
        for chars in zip(*strs):
            if all(map(lambda x:x==chars[0], chars)):
                prefix += chars[0]
            else:
                break
        return prefix