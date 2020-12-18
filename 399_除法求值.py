from typing import List

from collections import deque
class Solution:
    def calcEquation(self, equations: List[List[str]], 
        values: List[float], queries: List[List[str]]) -> List[float]:

        self.adjacent_matrix = {}
        for equation, value in zip(equations, values):
            self.adjacent_matrix.setdefault(equation[0],{})[equation[1]] = value
            if value == 0:
                self.adjacent_matrix[equation[1]] = 0
            else:
                self.adjacent_matrix.setdefault(equation[1],{})[equation[0]] = 1./value

        ret = []
        dividend_q = deque()
        value_q = deque()
        for dividend, divisor in queries:
            visited = {dividend,}
            if dividend not in self.adjacent_matrix:
                ret.append(-1)
                continue
            elif self.adjacent_matrix[dividend] == 0:
                ret.append(0)
                continue
            elif dividend == divisor:
                ret.append(1)
                continue
            dividend_q.extend(list(self.adjacent_matrix[dividend].keys()))
            value_q.extend(list(self.adjacent_matrix[dividend].values()))
            while(len(dividend_q)>0):
                temp = dividend_q.popleft()
                temp_value = value_q.popleft()
                if temp == divisor:
                    ret.append(temp_value)
                    break
                # if temp not in self.adjacent_matrix[dividend]:
                    # self.adjacent_matrix[dividend][temp] = 
                visited.add(temp)
                for k, v in self.adjacent_matrix[temp].items():
                    if k in visited:
                        continue
                    dividend_q.append(k)
                    value_q.append(temp_value*v)
            else:
                ret.append(-1)

            dividend_q.clear()
            value_q.clear()
        return ret

equations = [["a","b"],["b","c"]]
values = [2.0,3.0]
queries = [["a","c"],["b","a"],["a","e"],["a","a"],["x","x"]]

sol = Solution()
ans = sol.calcEquation(equations, values, queries)
print(ans)

