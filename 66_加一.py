from typing import List

class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        if digits[-1] < 9:
            digits[-1] += 1
            return digits
        carry = 1
        for idx in range(len(digits))[::-1]:
            digits[idx], carry = self.corefunc(digits[idx], carry)
        if carry != 0:
            digits.insert(0, carry)
        return digits

    def corefunc(self, digit: int, carry: int):
        result = digit + carry
        if result >= 10:
            return result - 10, 1
        else:
            return result, 0

sol = Solution()
print(sol.plusOne([9,8,9]))