
from typing import List

class Solution:
    used = set()
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        basic_lessons = self.find_basic_lesson(prerequisites)
        while(len(basic_lessons)):
            self.used.add(basic_lessons.pop())
            if len(basic_lessons) == 0:
                basic_lessons = self.find_basic_lesson(prerequisites)
        return len([x for _, x in prerequisites if x not in self.used]) == 0

    def find_basic_lesson(self, prerequisites):
        return set([x[1] for x in prerequisites if x[1] not in self.used]) - \
            set([x[0] for x in prerequisites if x[1] not in self.used])


if __name__ == "__main__":
    sol = Solution()
    ans = sol.canFinish(4, [[1,0],[0,1]])
    print(ans)
