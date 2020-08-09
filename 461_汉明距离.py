class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        binDiff = x^y
        cnt = 0
        while(binDiff):
            if binDiff % 2:
                cnt += 1
            binDiff = binDiff >> 1
        return cnt