from typing import List

class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        lookup_table = {}
        relative_sort_list = []
        for num in arr1:
            lookup_table[num] = lookup_table.setdefault(num, 0) + 1
        for num in arr2:
            relative_sort_list += [num,] * lookup_table[num]
            lookup_table.pop(num)
        for num in sorted(lookup_table.keys()):
            relative_sort_list += [num,] * lookup_table[num]
        return relative_sort_list

sol = Solution()
ans = sol.relativeSortArray(arr1 = [2,3,1,3,2,4,6,7,9,2,19], arr2 = [2,1,4,3,9,6])
print(ans)