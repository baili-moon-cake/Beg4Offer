from typing import List

from collections import Counter
import heapq


class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        self.remains = Counter(tasks)
        for k in self.remains:
            self.remains[k] = (self.remains[k], 0)
        
        steps = 0
        while(self.remains):
            steps += 1
            _task, _maxcnts = None, 0
            for task, (cnts, interval) in self.remains.items():
                if interval == 0 and cnts > _maxcnts:
                    _maxcnts = cnts
                    _task = task
                elif interval > 0:
                    self.remains[task][1] -= 1
            self.remains[_task][0] -= 1
            if self.remains[_task][0] == 0:
                self.remains.pop(_task)
        return steps

sol = Solution()
tasks = ["A","A","A","B","B","B"]
n = 2
ans = sol.leastInterval(tasks, n)
print(ans)