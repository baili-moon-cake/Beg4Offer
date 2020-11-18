from typing import List

class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        if sum(gas) < sum(cost):
            return -1
        length = len(gas)
        start_pos = -1
        acc_gas = 0
        for pos in range(length):
            acc_gas +=  gas[pos] - cost[pos]
            if acc_gas >=0 and start_pos==-1:
                start_pos = pos
            elif acc_gas >=0:
                pass
            else:
                start_pos = -1
                acc_gas = 0
        return start_pos

sol = Solution()
gas  = [1,2,3,4,5]
cost = [3,4,5,1,2]
ans = sol.canCompleteCircuit(gas, cost)
print(ans)
