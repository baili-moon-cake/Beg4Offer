from typing import List

from collections import deque 

class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        g.sort()
        s.sort()
        child_length = len(g)
        ret = 0
        for cookie_size in s:
            if cookie_size >= g[ret]:
                ret += 1
            if ret == child_length:
                break
        return ret
