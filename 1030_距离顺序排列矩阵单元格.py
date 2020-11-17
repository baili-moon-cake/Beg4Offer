from typing import List


from itertools import product
class Solution:
    def allCellsDistOrder(self, R: int, C: int, r0: int, c0: int) -> List[List[int]]:
        return list(sorted(product(range(R), range(C)), key=lambda x,y:abs(x-r0)+abs(y-c0)))