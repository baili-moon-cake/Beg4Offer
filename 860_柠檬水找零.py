from typing import List

class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        profit_list = {5:0, 10:0,}
        for bill in bills:
            if bill == 5:
                profit_list[5] += 1
            elif bill == 10:
                profit_list[5] -= 1
                if profit_list[5] < 0:
                    return False
                profit_list[10] += 1
            else:
                if profit_list[10] > 0:
                    profit_list[10] -= 1
                    profit_list[5] -= 1
                    if profit_list[5] < 0:
                        return False
                else:
                    profit_list[5] -= 3
                    if profit_list[5] < 0:
                        return False
        return True
