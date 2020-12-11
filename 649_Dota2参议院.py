from collections import deque

class Solution:
    def predictPartyVictory(self, senate: str) -> str:
        radiant_senate_q, dire_senate_q = deque(), deque()
        for idx, char in enumerate(senate):
            if char == 'R':
                radiant_senate_q.append(idx)
            else:
                dire_senate_q.append(idx)
        length = len(senate)
        while(len(radiant_senate_q)>0 and len(dire_senate_q)>0):
            r, d = radiant_senate_q.popleft(), dire_senate_q.popleft()
            if r < d:
                radiant_senate_q.append(r+length)
            else:
                dire_senate_q.append(d+length)
        if len(radiant_senate_q) > 0:
            return "Radiant"
        else:
            return "Dire"

