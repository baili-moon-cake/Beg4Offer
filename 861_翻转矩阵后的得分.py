from typing import List

class Solution:
    def matrixScore(self, A: List[List[int]]) -> int:
        n, m = len(A), len(A[0])
        res = n

        for i in range(1, m):
            res <<= 1
            s = sum([A[j][i] ^ A[j][0] for j in range(n)])
            res += max(s, n - s)
        
        return res
