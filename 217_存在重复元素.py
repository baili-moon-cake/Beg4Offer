from typing import List

class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        hash_table = {,}
        for num in nums:
            if num not in hash_table:
                hash_table.add(num)
            else:
                return True

