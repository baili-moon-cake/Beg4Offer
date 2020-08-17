import bisect
class MinStack:
    def __init__(self):
        """
        initialize your data structure here.
        """
        self.list = []
        self.sortedList = []

    def push(self, x: int):
        self.list.append(x)
        bisect.insort_left(self.sortedList,x)

    def pop(self):
        ret = self.list.pop()
        self.sortedList.remove(ret)
        return ret

    def top(self):
        return self.list[-1]

    def getMin(self):
        return self.sortedList[0]