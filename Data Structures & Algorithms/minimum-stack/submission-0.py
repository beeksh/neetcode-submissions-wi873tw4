class MinStack:

    def __init__(self):
        self.arr = []
        self.minarr = []

    def push(self, val: int) -> None:
        self.arr.append(val)
        if len(self.minarr)>0:
            if val<self.minarr[-1]:
                self.minarr.append(val)
            else:
                self.minarr.append(self.minarr[-1])
        else:
            self.minarr.append(val)

    def pop(self) -> None:
        self.arr = self.arr[:-1]
        self.minarr = self.minarr[:-1]

    def top(self) -> int:
        return self.arr[-1]

    def getMin(self) -> int:
        return self.minarr[-1]
        