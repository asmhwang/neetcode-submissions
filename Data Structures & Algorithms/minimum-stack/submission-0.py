class MinStack:

    def __init__(self):
        self.stack = [] 
    def push(self, val: int) -> None:
        if not self.stack:
            cmin = val
        else:
            cmin = self.getMin()
            if val<cmin:
                cmin= val
        self.stack.append((val, cmin))
    def pop(self) -> None:
        return self.stack.pop()

    def top(self) -> int:
        return self.stack[-1][0]

    def getMin(self) -> int:
        return self.stack[-1][1]
